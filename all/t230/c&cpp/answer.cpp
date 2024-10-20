#include <iostream>
#include <regex>
#include <string>

std::string moveEmojisToEnd(const std::string& text) {
    // Regular expression to match emojis
    std::regex emojiRegex(R"([\x{1F600}-\x{1F64F}\x{1F300}-\x{1F5FF}\x{1F680}-\x{1F6FF}\x{2600}-\x{26FF}\x{2700}-\x{27BF}])", std::regex_constants::ECMAScript | std::regex_constants::icase);

    std::smatch matches;
    std::string result;

    // Find all emojis in the text
    auto words_begin = std::sregex_iterator(text.begin(), text.end(), emojiRegex);
    auto words_end = std::sregex_iterator();

    // Collect non-emoji characters first
    for (std::sregex_iterator i = words_begin; i != words_end; ++i) {
        matches = *i;
        size_t pos = matches.position();
        if (pos > 0) {
            result += text.substr(0, pos);
            break;
        }
    }

    // Append remaining non-emoji characters
    if (!result.empty()) {
        result += text.substr(result.size());
    } else {
        result = text;
    }

    // Append all emojis at the end
    for (std::sregex_iterator i = words_begin; i != words_end; ++i) {
        matches = *i;
        result += matches.str();
    }

    return result;
}