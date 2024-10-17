#include <iostream>
#include <string>
#include <openssl/md5.h> // Make sure to link against OpenSSL

// Function to compute and return the MD5 hash of the input string
std::string compute_md5(const std::string& input_string) {
    unsigned char digest[MD5_DIGEST_LENGTH];
    MD5((unsigned char*)input_string.c_str(), input_string.length(), (unsigned char*)&digest);

    char mdString[33];
    for(int i = 0; i < 16; ++i)
        sprintf(&mdString[i*2], "%02x", (unsigned int)digest[i]);

    return std::string(mdString);
}
