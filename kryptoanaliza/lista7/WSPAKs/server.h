#ifndef server_h
#define server_h

#include <netinet/in.h>
#include <sys/socket.h>

#include <wolfssl/options.h>
#include <wolfssl/ssl.h>

struct Server {
  int domain;
  int service;
  int protocol;
  u_long interface;
  int port;
  int backlog;

  struct sockaddr_in address;

  int socket;
  WOLFSSL_CTX *ctx; // Dodanie contextu WOLFSSL
  WOLFSSL *ssl;     // tls session

  void (*launch)(struct Server *server);
};

struct Server server_constructor(int domain, int service, int protocol,
                                 u_long interface, int port, int backlog,
                                 void (*launch)(struct Server *server));

#endif