#include <iostream>
#include <string>
#include <regex>
#include <algorithm>

std::string compressHtml(const std::string& html) {
    std::string result = html;

    // Remove all newline and tab characters from the string
    result = std::regex_replace(result, std::regex("[\r\n\t]+"), "");

    // Replace multiple consecutive spaces with a single space
    result = std::regex_replace(result, std::regex(" {2,}"), " ");

    // Remove spaces between HTML tags (e.g., transforming "> <" into "><")
    result = std::regex_replace(result, std::regex("> <+"), "><");

    // Trim any leading and trailing whitespace from the final string
    auto start = result.find_first_not_of(" \n\r\t");
    auto end = result.find_last_not_of(" \n\r\t");
    result = (start == std::string::npos) ? "" : result.substr(start, end - start + 1);

    return result;
}

int main() {
    std::string html = "<html>   \n   <body>  \n  <h1>    Hello, World!   </h1>   \n   </body>   \n</html>";
    std::string compressedHtml = compressHtml(html);
    std::cout << compressedHtml << std::endl;
    return 0;
}