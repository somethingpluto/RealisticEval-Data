/**
 * @brief Reads a CSV file and parses each line into a vector of strings.
 *
 * @param file_path The path to the CSV file.
 * @return A vector of vector of strings, where each vector represents a line from the CSV.
 */
std::vector<std::vector<std::string>> read_csv(const std::string& file_path);