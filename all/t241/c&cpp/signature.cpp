/**
 * @brief Finds the minimum distance between two words in a text file, considering each line as a separate sequence.
 *
 * @param file_path The path to the file to read.
 * @param word1 The first word to search for.
 * @param word2 The second word to search for.
 *
 * @return A tuple containing the line number with the minimum distance and the minimum distance itself.
 *         Returns (std::nullopt, std::numeric_limits<int>::max()) if one or both words are not found in any line.
 */
std::tuple<std::optional<int>, int> get_min_seq_num_and_distance(const std::string& file_path, const std::string& word1, const std::string& word2){

}