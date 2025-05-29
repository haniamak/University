// Hanna Makowska 340547

#include <arpa/inet.h> // definiuje inet_ntop()
#include <errno.h> // definiuje errno -> przechowuje kod bledu
#include <netinet/ip.h> // definiuje strukture struct ip do obslugi naglowkow IP
#include <stdio.h>  // definiuje funkcje printf(), fprintf()
#include <stdlib.h> // definiuje funkcje exit(), EXIT_FAILURE -> do konczneia programu
#include <string.h> // definiuje funkcje strerror() -> do obslugi bledow
#include <assert.h> // definiuje funkcje assert() -> do obslugi bledow
#include <netinet/ip_icmp.h> // definiuje strukture struct icmp do obslugi naglowkow ICMP
#include <unistd.h> // definiuje funkcje systempowe typu close albo getpid
#include <sys/time.h>  // do obsługi czasu
#include <poll.h> // do obslugi poll()

#define MAX_TTL 30
#define TIMEOUT_MS 1000
#define PACKETS_PER_TTL 3
const int WORD_SIZE = 4;

// strukt do przechowywania informacji o pakiecie
struct packet_info {
  struct timeval send_time;
  char ip[INET_ADDRSTRLEN]; // adres odbiorcy
  struct timeval recv_time;
  u_int16_t seq;
};

// funkcja ze skosa do obliczania sumy kontrolnej dla naglowka ICMP
u_int16_t compute_icmp_checksum(const void *buff, int length)
{
  const u_int16_t *ptr = buff;
  u_int32_t sum = 0;
  assert(length % 2 == 0);
  for (; length > 0; length -= 2)
    sum += *ptr++;
  sum = (sum >> 16U) + (sum & 0xffffU);
  return (u_int16_t)(~(sum + (sum >> 16U)));
}

// funkcja ze skosa do obslugi bledow
void ERROR(const char *str)
{
  fprintf(stderr, "%s: %s\n", str, strerror(errno));
  exit(EXIT_FAILURE);
}

// funkcja ze skosa do wypisywania zawartosci bufora w postaci bajtow
void print_as_bytes(unsigned char *buff, ssize_t length)
{
  for (ssize_t i = 0; i < length; i++, buff++)
    printf("%.2x ", *buff);
}

// WYSYLANIE PAKIETU

void send_packet(int socketfiledescriptor, struct icmp *header, struct sockaddr_in *recipient, struct packet_info *packet, int seq) {
  header->icmp_hun.ih_idseq.icd_seq = seq;
  packet->seq = seq;

  header->icmp_cksum = 0;
  header->icmp_cksum = compute_icmp_checksum((u_int16_t*)header, sizeof(*header));

  gettimeofday(&packet->send_time, NULL);

  ssize_t bytes_sent = sendto(socketfiledescriptor, header, sizeof(*header), 0, (struct sockaddr*)recipient, sizeof(*recipient));
  if (bytes_sent < 0)
    ERROR("sendto error");
}

void send_icmp_packets(int socketfiledescriptor, const char *dest_ip, struct packet_info packet_times[PACKETS_PER_TTL], int timetolive) {
  struct icmp header; // tworzymy naglowek ICMP
  memset(&header, 0, sizeof(header));
  header.icmp_type = 8; // ICMP_ECHO
  header.icmp_code = 0;
  header.icmp_hun.ih_idseq.icd_id = getpid() & 0xFFFF; // 16 bajtow z processId na ustawienie id

  struct sockaddr_in recipient; // tworzymy strukture adresu odbiorcy
  memset(&recipient, 0, sizeof(recipient));
  recipient.sin_family = AF_INET; // ustawiamy rodzaj adresu na IPv4
  inet_pton(AF_INET, dest_ip, &recipient.sin_addr); // konwertujemy adres na postac binarna

  setsockopt(socketfiledescriptor, IPPROTO_IP, IP_TTL, &timetolive, sizeof(timetolive)); // ustawiamy timetolive

  for (int i = 0; i < PACKETS_PER_TTL; i++) {
    send_packet(socketfiledescriptor, &header, &recipient, &packet_times[i], timetolive * PACKETS_PER_TTL + i);
  }
}

void extract_icmp_info(const u_int8_t *buffer, struct ip *ip_header, u_int16_t *seq, u_int16_t *id) {
  struct icmp *icmp_header = (struct icmp *)(buffer + WORD_SIZE * ip_header->ip_hl);

  if (icmp_header->icmp_type == ICMP_TIME_EXCEEDED) {
    struct ip *ip_header2 = (struct ip *)(buffer + sizeof(struct icmphdr) + ip_header->ip_hl * WORD_SIZE);
    u_int8_t *icmp_packet2 = ((u_int8_t *)buffer + sizeof(struct icmphdr) + ip_header->ip_hl * WORD_SIZE) + WORD_SIZE * ip_header2->ip_hl;
    struct icmp *icmp_header2 = (struct icmp *)icmp_packet2;
    *seq = icmp_header2->icmp_hun.ih_idseq.icd_seq;
    *id = icmp_header2->icmp_hun.ih_idseq.icd_id;
  } else if (icmp_header->icmp_type == ICMP_ECHOREPLY) {
    *seq = icmp_header->icmp_hun.ih_idseq.icd_seq;
    *id = icmp_header->icmp_hun.ih_idseq.icd_id;
  } else {
    printf("Unknown ICMP type\n");
  }
}

void receive_icmp_packets(int socketfiledescriptor, struct packet_info packets[PACKETS_PER_TTL], int processId) {
  struct sockaddr_in sender;
  socklen_t sender_len = sizeof(sender);
  u_int8_t buffer[IP_MAXPACKET];

  struct pollfd poll_struct;
  poll_struct.fd = socketfiledescriptor;
  poll_struct.events = POLLIN;
  poll_struct.revents = 0;
  int responses_received = 0;

  while (responses_received < PACKETS_PER_TTL) {
    int ready = poll(&poll_struct, 1, TIMEOUT_MS);
    if (ready == -1) {
      ERROR("poll error");
    } else if (ready == 0) {
      // printf("timetolive %d: Timeout\n", timetolive);
      break;
    }
    
    // czas polla nie wiemy jeszcze ktory to bedzie pakiet
    struct timeval current_time;
    gettimeofday(&current_time, NULL);

    ssize_t packet_len = recvfrom(socketfiledescriptor, buffer, IP_MAXPACKET, 0, (struct sockaddr*)&sender, &sender_len);
    if (packet_len < 0) {
      ERROR("recvfrom error");
    }

    char sender_ip_str[INET_ADDRSTRLEN];
    inet_ntop(AF_INET, &(sender.sin_addr), sender_ip_str, sizeof(sender_ip_str));

    struct ip* ip_header = (struct ip*) buffer;

    u_int16_t seq;
    u_int16_t id;
    extract_icmp_info(buffer, ip_header, &seq, &id);

    // przejdz przez wszystkie pakiety w tablicy i sprawdzic seq i id i zapisac czas i skad przyszedl
    for (int i = 0; i < PACKETS_PER_TTL; i++) {
      if (packets[i].seq == seq && id == (processId & 0xFFFF)) {
        packets[i].recv_time = current_time;
        strcpy(packets[i].ip, sender_ip_str);
        responses_received++;
        break;
      }
    }
  }
}

void print_trace_result(int timetolive, int rtt_count, char unique_ips[PACKETS_PER_TTL][INET_ADDRSTRLEN], int unique_count, double rtt_sum, const char *dest_ip, int socketfiledescriptor) {
  printf("%d. ", timetolive);
  if (rtt_count == 0) {
    printf("*\n");
  } 
  else {
    for (int i = 0; i < unique_count; i++) {
      printf("%s ", unique_ips[i]);
    }
    if (rtt_count < PACKETS_PER_TTL) {
      printf("???\n");
    } else {
      printf("%.3f ms\n", rtt_sum / rtt_count);
    }
    // zakończ jeśli dotarłeś do hosta docelowego
    for (int i = 0; i < unique_count; i++) {
      if (strcmp(unique_ips[i], dest_ip) == 0) {
        close(socketfiledescriptor);
        exit(0);
      }
    }
  }
}

int main(int argc, char *argv[]) {
  if (argc != 2) {
    fprintf(stderr, "Usage: %s <destination_ip>\n", argv[0]);
    exit(EXIT_FAILURE);
  }

  if (inet_aton(argv[1], NULL) == 0) {
    fprintf(stderr, "Destination IP is unknown\n");
    exit(EXIT_FAILURE);
  }

  const char *dest_ip = argv[1];
  int socketfiledescriptor = socket(AF_INET, SOCK_RAW, IPPROTO_ICMP);
  if (socketfiledescriptor < 0)
    ERROR("socket error");

  int processId = getpid();

  for (int timetolive = 1; timetolive <= MAX_TTL; timetolive++) {
    struct packet_info packets[PACKETS_PER_TTL];
    memset(packets, 0, sizeof(packets)); // zerujemy tablice pakietow
    send_icmp_packets(socketfiledescriptor, dest_ip, packets, timetolive);
    receive_icmp_packets(socketfiledescriptor, packets, processId);

    // Zbierz unikalne IP
    char unique_ips[PACKETS_PER_TTL][INET_ADDRSTRLEN] = { "", "", "" };
    int unique_count = 0;
    double rtt_sum = 0;
    int rtt_count = 0;

    for (int i = 0; i < PACKETS_PER_TTL; i++) {
      if (strlen(packets[i].ip) > 0) {
        int found = 0;
        for (int j = 0; j < unique_count; j++) {
          if (strcmp(packets[i].ip, unique_ips[j]) == 0) {
            found = 1;
            break;
          }
        }
        if (!found) {
          strcpy(unique_ips[unique_count++], packets[i].ip);
        }

        long seconds = packets[i].recv_time.tv_sec - packets[i].send_time.tv_sec;
        long microseconds = packets[i].recv_time.tv_usec - packets[i].send_time.tv_usec;
        double elapsed = seconds + microseconds / 1000000.0;
        rtt_sum += (elapsed * 1000);
        rtt_count++;
      }
    }

    // Wypisz wynik dla timetolive
    print_trace_result(timetolive, rtt_count, unique_ips, unique_count, rtt_sum, dest_ip, socketfiledescriptor);
  }

  close(socketfiledescriptor);
  return 0;
}

