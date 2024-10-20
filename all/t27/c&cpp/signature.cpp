/**
 * @brief Concatenates JSON arrays from all JSON files in a specified directory.
 * 
 * This function iterates through all the files in the given directory, 
 * reads the contents of each JSON file, and combines all the arrays 
 * found at the root level of each file into a single vector.
 *
 * @param directory The path to the directory containing the JSON files.
 * @return A vector containing all the JSON objects found in the arrays 
 *         across the JSON files in the specified directory.
 */
std::vector<Json::Value> concatenate_json_arrays(const std::string &directory) {}