
/**
 * @brief Reads a file from the specified path, processes each line to remove inline comments,
 * removes line breaks, and returns a list of the processed line contents.
 *
 * @param path The path to the file to be read.
 * @return std::vector<std::string> A vector of strings, each representing a processed line from the file.
 */
std::vector<std::string> read_file_and_process_lines(const std::string& path);