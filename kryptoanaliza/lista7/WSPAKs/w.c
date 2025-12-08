#include <arpa/inet.h>
#include <stdio.h>
#include <unistd.h>
#include <wolfssl/options.h>
#include <wolfssl/ssl.h>
#include <wolfssl/wolfio.h>

#define PORT 8443

int main() {
  int sockfd, clientfd;
  socklen_t cli_len;
  struct sockaddr_in addr, cli_addr;

  wolfSSL_Init();

  /* Tworzymy kontekst TLS (serwer) */
  WOLFSSL_CTX *ctx = wolfSSL_CTX_new(wolfTLSv1_3_server_method());
  if (!ctx) {
    printf("wolfSSL_CTX_new error\n");
    return -1;
  }

  /* Ładujemy certyfikat i klucz */
  if (wolfSSL_CTX_use_certificate_file(ctx, "server-cert.pem",
                                       SSL_FILETYPE_PEM) != WOLFSSL_SUCCESS ||
      wolfSSL_CTX_use_PrivateKey_file(ctx, "server-key.pem",
                                      SSL_FILETYPE_PEM) != WOLFSSL_SUCCESS) {
    printf("Error loading cert or key\n");
    return -1;
  }

  /* Tworzymy socket TCP */
  sockfd = socket(AF_INET, SOCK_STREAM, 0);

  addr.sin_family = AF_INET;
  addr.sin_port = htons(PORT);
  addr.sin_addr.s_addr = INADDR_ANY;

  bind(sockfd, (struct sockaddr *)&addr, sizeof(addr));
  listen(sockfd, 1);

  printf("Server listening on port %d...\n", PORT);

  cli_len = sizeof(cli_addr);
  clientfd = accept(sockfd, (struct sockaddr *)&cli_addr, &cli_len);

  /* Tworzymy obiekt SSL dla połączenia */
  WOLFSSL *ssl = wolfSSL_new(ctx);
  wolfSSL_set_fd(ssl, clientfd);

  if (wolfSSL_accept(ssl) != WOLFSSL_SUCCESS) {
    printf("TLS handshake failed.\n");
    wolfSSL_free(ssl);
    close(clientfd);
    return -1;
  }

  printf("TLS handshake successful!\n");

  /* Odbieramy dane */
  char buffer[1024];
  int recv_len = wolfSSL_read(ssl, buffer, sizeof(buffer) - 1);
  if (recv_len > 0) {
    buffer[recv_len] = 0;
    printf("Client says: %s\n", buffer);

    /* Odpowiadamy */
    wolfSSL_write(ssl, "Hello from WolfSSL server!\n", 28);
  }

  wolfSSL_free(ssl);
  close(clientfd);
  close(sockfd);
  wolfSSL_CTX_free(ctx);
  wolfSSL_Cleanup();

  return 0;
}
