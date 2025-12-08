#include "server.h"
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
#include <wolfssl/ssl.h>

void sigchld_handler(int sig) { // zapobiega zombie
  while (waitpid(-1, 0, WNOHANG) > 0)
    continue;
}

ssize_t ssl_write_all(WOLFSSL *ssl, const void *buf, size_t len) {
  size_t total_sent = 0;

  while (total_sent < len) {
    int ret =
        wolfSSL_write(ssl, (const char *)buf + total_sent, len - total_sent);

    if (ret <= 0) {
      int err = wolfSSL_get_error(ssl, ret);
      if (err == WOLFSSL_ERROR_WANT_READ || err == WOLFSSL_ERROR_WANT_WRITE) {
        continue; // spróbuj ponownie
      }
      return -1; // błąd
    }

    total_sent += ret;
  }
  return total_sent;
}

// int reverse_line(WOLFSSL *ssl, int position) {
//   while (1) {
//     char line[65535] = {0};
//     char reverse_line[65535] = {0};

//     ssize_t bytes = wolfSSL_read(ssl, &line, 65535); // czytanie z ssl

//     if (bytes <= 0) {
//       printf("SSL read error or connection closed\n");
//       return -1; // błąd lub zamknięcie połączenia
//     }

//     position = bytes - 2;

//     if (position < 0) {
//       printf("empty line\n");
//       return -1; // zła linia
//     }

//     int len = position;
//     for (int i = 0; i < len; i++) {
//       reverse_line[i] = line[len - i];
//     }
//     reverse_line[len] = '\r';
//     reverse_line[len + 1] = '\n';

//     // TODO : sprawdzic czy wszystko zostalo wyslane
//     if (ssl_write_all(ssl, reverse_line, len + 2) < 0) {
//       fprintf(stderr, "SSL write error\n");
//       return -1;
//     }

//     position = 0;
//   }
//   return 0;
// }

int reverse_line(WOLFSSL *ssl) {
  while (1) {
    char line[65535] = {0};
    char reverse_line[65535] = {0};

    ssize_t bytes = wolfSSL_read(ssl, line, sizeof(line));
    if (bytes <= 0) {
      printf("SSL read error or connection closed\n");
      return -1;
    }

    int len;

    // CRLF
    if (bytes >= 2 && line[bytes - 2] == '\r' && line[bytes - 1] == '\n') {
      len = bytes - 2;
    }
    // tylko LF
    else if (line[bytes - 1] == '\n') {
      len = bytes - 1;
    } else {
      printf("Invalid line ending\n");
      return -1;
    }

    if (len <= 0) {
      break; // pusta linia → ignoruj
    }

    // Odwracanie prawidłowe
    for (int i = 0; i < len; i++) {
      reverse_line[i] = line[len - 1 - i];
    }

    // Dodaj tylko LF
    reverse_line[len] = '\n';

    // Wyślij
    if (ssl_write_all(ssl, reverse_line, len + 1) < 0) {
      fprintf(stderr, "SSL write error\n");
      return -1;
    }
  }

  return 0;
}

void launch(struct Server *server) {

  while (1) {
    printf("Waiting for TLS connection...\n");

    struct sockaddr_in client_address;
    socklen_t client_len = sizeof(client_address);

    int new_socket;
    while (1) {
      new_socket = accept(server->socket, (struct sockaddr *)&client_address,
                          &client_len);

      if (new_socket < 0) {
        if (errno == EINTR) {
          continue; // ponów accept()
        }
        perror("Failed to accept connection");
        break;
      }
      break; // accept OK
    }

    pid_t pid = fork();

    if (pid < 0) {
      perror("fork failed");
      close(new_socket);
      continue;
    }

    if (pid == 0) {
      close(server->socket);

      WOLFSSL *ssl =
          wolfSSL_new(server->ctx); // Utworzenie nowej struktury WOLFSSL
      if (!ssl) {
        printf("wolfSSL_new error\n");
        close(new_socket);
        exit(1);
      }

      wolfSSL_set_fd(ssl, new_socket); // Powiązanie WOLFSSL z gniazdem

      if (wolfSSL_accept(ssl) != SSL_SUCCESS) { // Przeprowadzenie TLS handshake
        printf("TLS handshake failed\n");
        wolfSSL_free(ssl);
        // wolfSSL_CTX_free(server->ctx);
        // wolfSSL_Cleanup();
        close(new_socket);
        exit(1);
      }

      int position = 0;

      if (reverse_line(ssl) < 1) {
        fprintf(stderr, "Error reversing line\n");
      }
      wolfSSL_shutdown(ssl);
      wolfSSL_free(ssl);
      close(new_socket);
      exit(0);
    } else {
      close(new_socket);
    }
  }
}

int main() {
  signal(SIGCHLD, sigchld_handler); // do zombie

  struct Server server =
      server_constructor(AF_INET, SOCK_STREAM, 0, INADDR_ANY, 7777, 10, launch);

  server.launch(&server);
}

// by skompilowac: gcc test.c server.c -lwolfssl -o server
// by odpalic: ./server

// w drugim terminalu; openssl s_client -connect localhost:7777
// openssl s_client -connect localhost:7777 -CAfile server-cert.pem
// albo bardziej tak
// potem wpisac linie do

// generowanie certyfikatu i klucza:
// openssl genrsa - out server - key.pem 2048 openssl req - new - x509 -
//    key server - key.pem - out server - cert.pem - days 365
