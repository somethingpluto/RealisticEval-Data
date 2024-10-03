#include <string>
#include <map>
#include <sstream>
#include <iostream>

std::map<std::string, std::string> parse_http_request_line(const std::string& response)
{
    // Initialize the result map
    std::map<std::string, std::string> result;

    // Step 1: Find the position of the first line of the response (request line)
    size_t end_of_first_line = response.find("\r\n");

    if (end_of_first_line == std::string::npos) {
        // If no valid line break is found, return an empty map
        return result;
    }

    // Step 2: Extract the first line (the request line)
    std::string request_line = response.substr(0, end_of_first_line);

    // Step 3: Split the request line into method, URL, and version
    std::istringstream line_stream(request_line);
    std::string method;
    std::string url;
    std::string http_version;

    // Parse method (e.g., GET, POST)
    line_stream >> method;

    // Parse URL (e.g., /index.html)
    line_stream >> url;

    // Parse HTTP version (e.g., HTTP/1.1)
    line_stream >> http_version;

    // Step 4: Store the parsed information in the result map
    result["method"] = method;
    result["url"] = url;
    result["http_version"] = http_version;

    // Step 5: Return the result map
    return result;
}