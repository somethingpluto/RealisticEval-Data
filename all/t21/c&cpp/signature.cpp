/**
 * @brief Compare the contents of two files and print the differences in unified diff format.
 *
 * @param file1_path Path to the first file.
 * @param file2_path Path to the second file.
 * @return std::vector<std::string> A vector containing the lines of differences, if any.
 * @throw std::runtime_error If either file does not exist or there is an error reading the files.
 */
std::vector<std::string> compareFiles(const std::string& file1_path, const std::string& file2_path);