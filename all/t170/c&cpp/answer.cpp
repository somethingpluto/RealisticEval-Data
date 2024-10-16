#include <string>
#include <regex>

std::string convert(const std::string& html) {
    std::string markdown = std::regex_replace(html, std::regex("(?i)<br\\s*/?>"), "\n");
    markdown = std::regex_replace(markdown, std::regex("(?i)<p>"), "");
    markdown = std::regex_replace(markdown, std::regex("(?i)</p>"), "\n\n");
    markdown = std::regex_replace(markdown, std::regex("(?i)<strong>"), "**");
    markdown = std::regex_replace(markdown, std::regex("(?i)</strong>"), "**");
    markdown = std::regex_replace(markdown, std::regex("(?i)<em>"), "*");
    markdown = std::regex_replace(markdown, std::regex("(?i)</em>"), "*");
    markdown = std::regex_replace(markdown, std::regex("(?i)<u>"), "*");
    markdown = std::regex_replace(markdown, std::regex("(?i)</u>"), "*");
    markdown = std::regex_replace(markdown, std::regex("(?i)<code>"), "`");
    markdown = std::regex_replace(markdown, std::regex("(?i)</code>"), "`");
    markdown = std::regex_replace(markdown, std::regex("(?i)<ul>"), "");
    markdown = std::regex_replace(markdown, std::regex("(?i)</ul>"), "");
    markdown = std::regex_replace(markdown, std::regex("(?i)<ol>"), "");
    markdown = std::regex_replace(markdown, std::regex("(?i)</ol>"), "");
    markdown = std::regex_replace(markdown, std::regex("(?i)<li>"), "* ");
    markdown = std::regex_replace(markdown, std::regex("(?i)</li>"), "\n");
    markdown = std::regex_replace(markdown, std::regex("(?i)<a\\s+href=\"([^\"]*)\">(.*?)</a>"), "[$2]($1)");

    return markdown;
};