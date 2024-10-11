/**
 * Logs an item by printing it. Handles strings, numbers, lists, and dictionaries by printing
 * them directly or as a JSON-formatted string. Other types are reported as errors.
 *
 * @param item The item to be logged. Can be of any type.
 * @return The item to be logged. Can be of any type.
 */
template<typename T>
T log(T item)
{
    // Convert item to JSON if necessary
    nlohmann::json jsonItem = item;

    // Print the JSON representation of the item
    std::cout << jsonItem.dump(4) << std::endl; // Indentation of 4 spaces

    return item;
}

// Specialization for vectors
template<typename T>
std::vector<T> log(std::vector<T> item)
{
    // Convert vector to JSON
    nlohmann::json jsonItem = item;

    // Print the JSON representation of the vector
    std::cout << jsonItem.dump(4) << std::endl; // Indentation of 4 spaces

    return item;
}

// Specialization for maps
template<typename K, typename V>
std::map<K, V> log(std::map<K, V> item)
{
    // Convert map to JSON
    nlohmann::json jsonItem = item;

    // Print the JSON representation of the map
    std::cout << jsonItem.dump(4) << std::endl; // Indentation of 4 spaces

    return item;
}