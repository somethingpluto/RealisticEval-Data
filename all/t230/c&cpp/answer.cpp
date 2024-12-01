#include <iostream>
#include <regex>
#include <string>

std::string move_emojis_to_end(const std::string& text) {
    /**
     * Move the emoji expressions in the string to the end of the text.
     *
     * Args:
     *     text (std::string): The input string containing text and possibly emojis.
     *
     * Returns:
     *     std::string: The modified string with all emojis moved to the end.
     */

    // Regular expression pattern for capturing emojis
    std::regex emoji_pattern(
        u"[\u2702-\u27B0"  // Dingbats
        u"\u24C2-\u1F251"  // Enclosed characters
        u"\u1F600-\u1F64F"  // Emoticons
        u"\u1F300-\u1F5FF"  // Symbols & Pictographs
        u"\u1F680-\u1F6FF"  // Transport & Map Symbols
        u"\u1F700-\u1F77F"  // Alchemical Symbols
        u"\u1F780-\u1F7FF"  // Geometric Shapes Extended
        u"\u1F800-\u1F8FF"  // Supplemental Arrows-C
        u"\u1F900-\u1F9FF"  // Supplemental Symbols and Pictographs
        u"\u1FA00-\u1FA6F"  // Chess Symbols
        u"\u1FA70-\u1FAFF"  // Symbols and Pictographs Extended-A
        "]+", std::regex::ECMAScript | std::regex::icase);

    // Find all emojis in the text
    std::smatch matches;
    std::string emojis;
    std::string::const_iterator searchStart(text.cbegin());
    while (std::regex_search(searchStart, text.cend(), matches, emoji_pattern)) {
        emojis += matches[0];
        searchStart = matches.suffix().first;
    }

    // Remove emojis from the text
    std::string text_without_emojis = std::regex_replace(text, emoji_pattern, "");

    // Concatenate non-emoji text with extracted emojis
    return text_without_emojis + emojis;
}
