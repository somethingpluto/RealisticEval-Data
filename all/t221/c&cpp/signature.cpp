/**
 * @brief Extract and parse strings containing Python dictionary syntax from a given file
 *
 * @param file_path The path to the file from which to extract dictionary strings.
 * @return A vector of maps representing the dictionaries extracted and parsed from the file.
 */
std::vector<std::map<std::string, std::string>> extractParseDictionaries(const std::string& file_path);