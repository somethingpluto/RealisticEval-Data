/**
 * Removes the extension of the given filename and returns the remainder
 *
 * @param file_name - The full name of the file from which to remove the extension.
 * @returns The file name without the extension. If no extension is found, returns the original file name.
 */
std::string removeFileExtension(const std::string& file_name);