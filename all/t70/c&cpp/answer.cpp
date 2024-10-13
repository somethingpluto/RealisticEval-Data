#include <iostream>
#include <regex>
#include <vector>
#include <string>

// Function to extract all code block contents from a markdown string
std::vector<std::string> code_block_remover(const std::string& markdown_string) {
    /**
     * Extracts all code block contents from a markdown string.
     *
     * Args:
     *     markdown_string (const std::string&): The input markdown string.
     *
     * Returns:
     *     std::vector<std::string>: A vector of strings, each representing the content of a code block.
     *                                Returns an empty vector if no code blocks are found.
     */
    
    // Define a pattern that captures content within triple backticks, with optional language specifier
    std::regex pattern(R"(```[a-zA-Z]*\n([\s\S]*?)```)");

    // Use std::sregex_iterator to find all occurrences of the pattern
    std::sregex_iterator matches_begin = std::sregex_iterator(markdown_string.begin(), markdown_string.end(), pattern);
    std::sregex_iterator matches_end = std::sregex_iterator();

    // Extract the matched groups and store them in a vector
    std::vector<std::string> code_blocks;
    for (std::sregex_iterator i = matches_begin; i != matches_end; ++i) {
        std::smatch match = *i;
        code_blocks.push_back(match[1].str());
    }

    return code_blocks;
}