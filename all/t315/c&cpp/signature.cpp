/**
 * Extract the fileId from the given URL query args. If not found, return an empty string.
 * For example:
 *      input: https://example.com/download?fileId=12345
 *      output: 12345
 *
 * @param std::string url - The URL from which the file ID is to be extracted.
 * @returns std::string - The extracted file ID if present, otherwise an empty string if the URL does not conform to the expected format.
 */
std::string getFileIdFromUrl(const std::string& url){}