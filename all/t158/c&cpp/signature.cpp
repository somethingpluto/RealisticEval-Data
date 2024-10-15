/**
 * Extract the file extension and return it if it exists. If not, an empty string is returned
 *
 * @param file_name - The full name of the file from which to extract the extension.
 * @returns The file extension without the dot, or an empty string if no extension is found.
 */
std::string getFileExtension(const std::string& file_name);