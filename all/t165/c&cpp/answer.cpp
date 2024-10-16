#include <string>
#include <algorithm>

std::string base64ToUrlSafe(const std::string& base64) {
    std::string urlSafeBase64 = base64;

    // Replace '+' with '-'
    std::replace(urlSafeBase64.begin(), urlSafeBase64.end(), '+', '-');

    // Replace '/' with '_'
    std::replace(urlSafeBase64.begin(), urlSafeBase64.end(), '/', '_');

    // Remove trailing '=' characters
    size_t pos = urlSafeBase64.find_last_not_of('=');
    if (pos != std::string::npos) {
        urlSafeBase64.erase(pos + 1);
    }

    return urlSafeBase64;
}