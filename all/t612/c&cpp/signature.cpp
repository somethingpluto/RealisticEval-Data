/**
 * @brief Finds and replaces text in a specified file.
 *
 * @param file_path The path to the file.
 * @param search_string The string to search for.
 * @param replace_string The string to replace with.
 *
 * @throws std::ios_base::failure If an I/O error occurs reading from the file or writing to the file.
 */
void find_and_replace_in_file(const std::string& file_path, const std::string& search_string, const std::string& replace_string);