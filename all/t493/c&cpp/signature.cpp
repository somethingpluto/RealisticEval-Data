/**
 * @brief Wraps the text content to the specified maximum width and generates lines one by one.
 *
 * @param content The content to be wrapped and yielded line by line.
 * @param width The maximum width of the lines. The default is 80 characters.
 *
 * @return Each line of the content wrapped to the specified width.
 */
std::string wrapText(const std::string &content, int width = 80);
