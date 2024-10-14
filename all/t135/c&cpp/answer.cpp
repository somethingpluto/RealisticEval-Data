#include <stdexcept>

bool isValidPortNumber(int port) {
    if (port < 1 || port > 65535) {
        throw std::invalid_argument("The port number must be between 1 and 65535.");
    }
    return true;
}