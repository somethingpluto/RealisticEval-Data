/**
 * @brief Extracts paragraphs and lines from the given text.
 * 
 * Paragraphs are defined as segments of text that end with "\n\n", 
 * and lines end with a single "\n".
 * 
 * @note Example:
 *     Input: "First paragraph.\nThis is the second line.\n\nSecond paragraph.\nAnother line."
 *     Output: (See function behavior for exact output structure)
 * 
 * @param text The input text from which paragraphs and lines will be extracted.
 * 
 * @return A map containing:
 *         - 'paragraphs': A vector of strings representing paragraphs extracted from the text.
 *         - 'lines': A vector of strings representing lines extracted from the text.
 */
std::map<std::string, std::vector<std::string>> extract_paragraphs_and_lines(const std::string& text);
