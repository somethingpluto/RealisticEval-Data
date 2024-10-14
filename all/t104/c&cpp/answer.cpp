#include <string>
#include <fstream>
#include <nlohmann/json.hpp>

using json = nlohmann::json;

/**
 * Converts a thread object to a JSON file represented as a string.
 * 
 * @param thread - The thread object to be converted.
 * @returns std::string - A string representing the JSON file.
 */
std::string convertThreadToJSONFile(const json& thread) {
    std::string jsonString = thread.dump();  // Convert the thread object to a JSON string
    return jsonString;  // Return the JSON string
}