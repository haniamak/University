#include "server.h"
#include <stdio.h>
#include <stdlib.h> // for exit()
#include <sys/types.h>

struct Server server_constructor(int domain, int service, int protocol,
                                 u_long interface, int port, int backlog,
                                 void (*launch)(struct Server *server)) {
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
  }

  server.launch = launch;

  return server;
};
