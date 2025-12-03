#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include "server.h"

void launch(struct Server *server)
{
  char line[65536];
  char reverse_line[65536];
  // char buffer[65535];

  // char *hello =
  //     "HTTP/1.1 200 OK\r\n"
  //     "Content-Type: text/plain\r\n"
  //     "Content-Length: 12\r\n"
  //     "Connection: close\r\n"
  //     "\r\n"
  //     "Hello world";

  while (1)
  {
    printf("Waiting for connection...\n");

    struct sockaddr_in client_address;
    socklen_t client_len = sizeof(client_address);

    int new_socket = accept(server->socket, (struct sockaddr *)&client_address, &client_len);
    if (new_socket < 0)
    {
      perror("Failed to accept connection");
      continue;
    }
    // int bytes = read(new_socket, buffer, sizeof(buffer) - 1);
    // if (bytes > 0)
    // {
    //   buffer[bytes] = '\0';
    //   printf("%s\n", buffer);
    // }

    // write(new_socket, hello, strlen(hello));
    // close(new_socket);
    int position = 0;
    while (1)
    {
      char c;
      int bytes = read(new_socket, &c, 1);

      if (bytes <= 0) {
        close(new_socket);
        break;
      }

      line[position++] = c;

      if (position >= 65535) {
        position = 0; // ? mam kontynuowac wywalic blad czy co
      }

      if (position >= 2 && line[position - 2] == '\r' && line[position - 1] == '\n') {
        if (position == 2) {
          // empty line, end of request
          close(new_socket);
          break;
        }

        int len = position - 2;
        for (int i = 0; i < len; i++) {
          reverse_line[i] = line[len - 1 - i];
        }
        reverse_line[len] = '\r';
        reverse_line[len + 1] = '\n';

        send(new_socket, reverse_line, len + 2, 0);
        position = 0;
      }

    }
  }
}

int main() {
  struct Server server = server_constructor(AF_INET, SOCK_STREAM, 0, INADDR_ANY, 7777, 10, launch);
  server.launch(&server);
}