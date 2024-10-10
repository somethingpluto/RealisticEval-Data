#include <iostream>
#include <regex>
#include <vector>
#include <string>

std::vector<std::string> code_block_remover(const std::string& markdown_string) {
    std::vector<std::string> code_blocks;
    std::regex code_block_regex(R"(```[\s\S]*?```)", std::regex_constants::ECMAScript);
    auto words_begin = std::sregex_iterator(markdown_string.begin(), markdown_string.end(), code_block_regex);
    auto words_end = std::sregex_iterator();

    for (std::sregex_iterator i = words_begin; i != words_end; ++i) {
        std::smatch match = *i;
        std::string matched_string = match.str();
        // Remove the ``` and ```, leaving only the code block content
        size_t start = 3;
        size_t end = matched_string.length() - 3;
        code_blocks.push_back(matched_string.substr(start, end));
    }

    return code_blocks;
}