/**
 * @brief Copies the contents of the source file to the destination file using a buffered stream
 * and measures the time it takes to complete the operation.
 *
 * @param source_file_path The path to the source file.
 * @param destination_file_path The path to the destination file.
 * @return The time taken to copy the file in milliseconds.
 */
int copy_file_with_buffered_stream(const std::string& source_file_path, const std::string& destination_file_path);