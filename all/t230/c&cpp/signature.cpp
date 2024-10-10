std::string moveEmojisToEnd(const std::string& text) {
    /*
    Move the emoj expression in the string to the end of the text

    Args:
        text (const std::string&): The input string containing text and possibly emojis.

    Returns:
        std::string: The modified string with all emojis moved to the end.
    */

    // Regex pattern to match any emoji character
    std::regex emojiPattern(R"([\x{1F600}-\x{1F64F}\x{1F300}-\x{1F5FF}\x{1F680}-\x{1F6FF}\x{2600}-\x{26FF}\x{2700}-\x{27BF}])", std::regex_constants::icase);
    return result;
}