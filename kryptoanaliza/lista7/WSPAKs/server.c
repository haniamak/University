#include "server.h"
#include <stdio.h>
#include <stdlib.h> // for exit()
#include <sys/socket.h>
#include <sys/types.h>

struct Server server_constructor(int domain, int service, int protocol,
                                 u_long interface, int port, int backlog,
                                 void (*launch)(struct Server *server)) {
  wolfSSL_Init(); // Inicjalizacja wolfSSL

  struct Server server;
  server.domain = domain;
  server.service = service;
  server.protocol = protocol;
  server.interface = interface;
  server.port = port;
  server.backlog = backlog;
  server.launch = launch;

  server.address.sin_family = domain;
  server.address.sin_port = htons(port);
  server.address.sin_addr.s_addr = interface;

  server.socket = socket(domain, service, protocol);

  if (server.socket < 0) {
    perror("Failed to connect socket");
    exit(1);
  }
  setsockopt(server.socket, SOL_SOCKET, SO_REUSEADDR, &(int){1},
             sizeof(int)); // aby ponownie uzyc portu

  if (bind(server.socket, (struct sockaddr *)&server.address,
           sizeof(server.address)) < 0) {
    perror("Failed to bind socket");
    exit(1);
  }

  if (listen(server.socket, server.backlog) < 0) {
    perror("Failed to listen on socket");
    exit(1);
    server.ctx = wolfSSL_CTX_new(wolfTLSv1_2_server_method());
    if (!server.ctx) {
      printf("wolfSSL_CTX_new error\n");
      exit(1);
    }
  }

  // Inicjalizacja kontekstu TLS
  server.ctx = wolfSSL_CTX_new(wolfTLSv1_2_server_method());
  if (!server.ctx) {
    printf("wolfSSL_CTX_new error\n");
    exit(1);
  }

  // Wczytanie certyfikatu
  if (wolfSSL_CTX_use_certificate_file(server.ctx, "server-cert.pem",
                                       SSL_FILETYPE_PEM) != SSL_SUCCESS) {
    printf("Error loading cert\n");
    exit(1);
  }

  // Wczytanie klucza prywatnego
  if (wolfSSL_CTX_use_PrivateKey_file(server.ctx, "server-key.pem",
                                      SSL_FILETYPE_PEM) != SSL_SUCCESS) {
    printf("Error loading key\n");
    exit(1);
  }

  server.launch = launch;

  return server;
};
