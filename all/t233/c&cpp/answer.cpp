#include <iostream>
#include <string>

std::string remove_comments(const std::string &input) {
    std::string result;
    bool inComment = false;

    for (size_t i = 0; i < input.length(); ++i) {
        if (inComment && input[i] == '\n') {
            // End of comment, skip to next line
            inComment = false;
            continue;
        }
        if (!inComment && input[i] == '#') {
            // Start of comment
            inComment = true;
            continue;
        }
        if (!inComment) {
            // Not in a comment, add character to result
            result += input[i];
        }
    }

    return result;
}