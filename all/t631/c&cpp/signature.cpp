/**
 * @brief Formats a list of strings into a single-line CSV string and writes it to a specified file.
 *
 * @param strings The vector of strings to be formatted into CSV.
 *                Must not be empty; an empty vector will result in no output.
 * @type strings const std::vector<std::string>&
 *
 * @param file_path The file path where the CSV string should be written.
 *                  Must be a valid file path that is accessible for writing.
 * @type file_path const std::string&
 *
 * @return void
 */

void write_csv_to_file(const std::vector<std::string>& strings, const std::string& file_path);