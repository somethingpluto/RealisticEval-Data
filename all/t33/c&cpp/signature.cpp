/**
 * @brief Converts the XML file into a vector of maps.
 *
 * Each <sequence> tag is treated as a row,
 * and the tag and text content of each sub-element are treated as columns and values of the map.
 *
 * @param xml_file The path to the XML file.
 * @return A vector of maps containing the data from the XML file.
 */
std::vector<std::map<std::string, std::string>> xml_to_vector_of_maps(const std::string& xml_file) {}