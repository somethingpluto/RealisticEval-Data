/**
 * @brief Reads data from a specified file and determines the type of each line.
 *
 * @param path The path to the file to be read. The file should exist and be 
 *             accessible for reading.
 * @type path const std::string&
 *
 * @return A vector containing the converted values of each line in the file. Each 
 *         element can be an `int`, `float`, or `std::string`, depending on the content 
 *         of the line.
 * @rtype std::vector<std::variant<int, float, std::string>>
 *
 * @throws std::runtime_error If the specified file does not exist or if there 
 *         is an error reading the file.
 */

std::vector<std::variant<int, float, std::string>> read_data_from_file(const std::string& path);