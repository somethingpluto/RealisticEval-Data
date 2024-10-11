/**
 * @brief Parses a markdown table from a given input string.
 *
 * This function takes a string representation of a markdown table and converts it
 * into a structured format, such as a 2D vector of strings. It processes the
 * table to extract headers and rows, handling various markdown table formatting
 * nuances.
 *
 * @param markdownTable A string containing the markdown table to be parsed.
 *                      The string should be properly formatted as a markdown table.
 *                      Example:
 *                      ```
 *                      | Header1 | Header2 |
 *                      |---------|---------|
 *                      | Row1Col1| Row1Col2|
 *                      | Row2Col1| Row2Col2|
 *                      ```
 *
 * @return A 2D vector of strings representing the parsed markdown table.
 *         The first sub-vector contains headers, and the subsequent sub-vectors
 *         contain the rows of the table.
 *
 * @throw std::invalid_argument if the input string is not a valid markdown table format.
 * @throw std::runtime_error if there is an issue during parsing, such as
 *         inconsistent row lengths.
 */
std::vector<std::vector<std::string>> parse_markdown_table(const std::string& markdownTable);
