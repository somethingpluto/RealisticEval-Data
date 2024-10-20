/**
 * @brief Modifies a specific line in the given file.
 *
 * @param filePath The path of the file to be modified.
 *                 Must be a valid file path leading to an accessible file.
 * @type filePath std::string
 *
 * @param lineNumber The line number to be modified (1-based index).
 *                   Must be greater than zero and within the total number of lines in the file.
 * @type lineNumber int
 *
 * @param newValue The new value to update the line with.
 * @type newValue std::string
 *
 * @return void
 */

void modifyLineInFile(const std::string& filePath, int lineNumber, const std::string& newValue);