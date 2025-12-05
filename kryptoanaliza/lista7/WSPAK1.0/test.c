#include "server.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

void sigchld_handler(int sig) { // zapobiega zombie
  while (waitpid(-1, 0, WNOHANG) > 0)
    continue;
}

void reverse_line(int new_socket, int position) {
  while (1) {
    char line[65535] = {0};
    char reverse_line[65535] = {0};

    ssize_t bytes = read(new_socket, &line, 65535);

    if (bytes <= 0) {
      close(new_socket);
      break;
    }

    position = bytes - 2;

    if (position < 0) {
      close(new_socket);
      break;
    }

    if (position == 2) {
      close(new_socket);
      break;
    }

    int len = position;
    for (int i = 0; i <= len; i++) {
      reverse_line[i] = line[len - i];
    }
    reverse_line[len + 1] = '\r';
    reverse_line[len + 2] = '\n';

    send(new_socket, reverse_line, len + 3, 0);
    position = 0;
  }
}

void launch(struct Server *server) {

  while (1) {
    printf("Waiting for connection...\n");

    struct sockaddr_in client_address;
    socklen_t client_len = sizeof(client_address);

    int new_socket =
        accept(server->socket, (struct sockaddr *)&client_address, &client_len);
    if (new_socket < 0) {
      perror("Failed to accept connection");
      continue;
    }

    pid_t pid = fork();

    if (pid < 0) {
      perror("fork failed");
      close(new_socket);
      continue;
    }

    if (pid == 0) {
      close(server->socket);

      int position = 0;

      reverse_line(new_socket, position);

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

// by skompilowac: gcc test.c server.c
// by odpalic: ./a.out

// w drugim terminalu; printf "Ala ma kota\r\n" | nc localhost 7777

// W TELNET : telnet localhost 7777
// by wyslac: Ala ma kota
// by zakonczyc: Ctrl + ]
// by wyjsc: quit