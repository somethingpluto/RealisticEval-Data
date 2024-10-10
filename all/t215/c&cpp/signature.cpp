/**
 * Replace words in a text file according to a dictionary map and return the modified text.
 *
 * @param file_path The path to the text file.
 * @param replacement_dict A dictionary where the keys are words to be replaced, and the values are the replacement words.
 * @return The text with the words replaced.
 */
std::string replaceWordsInFile(const std::string& file_path, const std::unordered_map<std::string, std::string>& replacement_dict);