#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include "server.h"

void launch(struct Server *server)
{
  char buffer[30000];

  char *hello =
      "HTTP/1.1 200 OK\r\n"
      "Content-Type: text/plain\r\n"
      "Content-Length: 12\r\n"
      "Connection: close\r\n"
      "\r\n"
      "Hello world";

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
    int bytes = read(new_socket, buffer, sizeof(buffer) - 1);
    if (bytes > 0)
    {
      buffer[bytes] = '\0';
      printf("%s\n", buffer);
    }

    write(new_socket, hello, strlen(hello));
    close(new_socket);
  }
}

int main() {
  struct Server server = server_constructor(AF_INET, SOCK_STREAM, 0, INADDR_ANY, 7777, 10, launch);
  server.launch(&server);
}