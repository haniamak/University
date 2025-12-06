#include "server.h"
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

void sigchld_handler(int sig) { // zapobiega zombie
  while (waitpid(-1, 0, WNOHANG) > 0)
    continue;
}

void reverse_line(WOLFSSL *ssl,
                  int position) { // juz nie prosty socket tylko WOLFSSL
  while (1) {
    char line[65535] = {0};
    char reverse_line[65535] = {0};

    ssize_t bytes = wolfSSL_read(ssl, &line, 65535); // czytanie z ssl

    if (bytes <= 0) {
      break;
    }

    position = bytes - 2;

    if (position < 0) {
      break;
    }

    if (position == 2) {
      break;
    }

    int len = position;
    for (int i = 0; i <= len; i++) {
      reverse_line[i] = line[len - i];
    }
    reverse_line[len + 1] = '\r';
    reverse_line[len + 2] = '\n';

    wolfSSL_write(ssl, reverse_line, len + 3);
    position = 0;
  }
}

void launch(struct Server *server) {

  while (1) {
    printf("Waiting for TLS connection...\n");

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
        close(new_socket);
        exit(1);
      }

      int position = 0;

      reverse_line(ssl, position);
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

// by skompilowac: cc test.c server.c -lwolfssl -o server
// by odpalic: ./server

// w drugim terminalu; openssl s_client -connect localhost:7777
// potem wpisac linie do odwrócenia