#include <iostream>
#include <cstring>
#include <sys/ioctl.h>
#include <net/if.h>
#include <arpa/inet.h>

std::string getLocalIP(const std::string &interface) {
    struct ifreq ifr;
    int fd;

    fd = socket(AF_INET, SOCK_DGRAM, 0);
    if (fd == -1) {
        perror("socket");
        return "Error";
    }

    memset(&ifr, 0, sizeof(ifr));
    strncpy(ifr.ifr_name, interface.c_str(), IFNAMSIZ-1);

    if (ioctl(fd, SIOCGIFADDR, &ifr) != 0) {
        close(fd);
        perror("ioctl");
        return "Error";
    }

    close(fd);

    char ip[INET_ADDRSTRLEN];
    inet_ntop(AF_INET, &((struct sockaddr_in *)&ifr.ifr_addr)->sin_addr, ip, INET_ADDRSTRLEN);
    
    return std::string(ip);
}