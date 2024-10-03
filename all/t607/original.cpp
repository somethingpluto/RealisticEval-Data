# code written with chatgpt

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>

#define HOST "localhost"
#define PORT_FROM 10000
#define PORT_TO 65000

int find_available_port() {
    struct sockaddr_in addr;
    int sock;
    for (int port = PORT_FROM; port <= PORT_TO; port++) {
        memset(&addr, 0, sizeof(addr));
        addr.sin_family = AF_INET;
        addr.sin_addr.s_addr = inet_addr(HOST);
        addr.sin_port = htons(port);
        sock = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
        if (sock < 0) {
            perror("socket");
            exit(1);
        }
        if (connect(sock, (struct sockaddr *)&addr, sizeof(addr)) < 0) {
            close(sock);
            return port;
        }
        close(sock);
    }
    return -1;
}