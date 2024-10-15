#include <iostream>
#include <string>
#include <regex>

std::string convertHtmlHeadingsToMarkdown(const std::string& html) {
    std::string markdown = html;

    // Replace h1 to h6 tags with corresponding Markdown headings using regex
    markdown = std::regex_replace(markdown, std::regex(R"(<h1>(.*?)<\/h1>)"), "# $1");
    markdown = std::regex_replace(markdown, std::regex(R"(<h2>(.*?)<\/h2>)"), "## $1");
    markdown = std::regex_replace(markdown, std::regex(R"(<h3>(.*?)<\/h3>)"), "### $1");
    markdown = std::regex_replace(markdown, std::regex(R"(<h4>(.*?)<\/h4>)"), "#### $1");
    markdown = std::regex_replace(markdown, std::regex(R"(<h5>(.*?)<\/h5>)"), "##### $1");
    markdown = std::regex_replace(markdown, std::regex(R"(<h6>(.*?)<\/h6>)"), "###### $1");

    return markdown;
}