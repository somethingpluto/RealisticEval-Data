#include <string>

std::string extract_json(const std::string& response) {
    auto start_pos = response.find('{'); // Find the position of the first '{'
    if (start_pos == std::string::npos) // If not found, return an empty string
        return "";

    int brace_count = 0; // To track the balance of braces
    size_t end_pos = start_pos; // Initialize end_pos to start_pos

    for (size_t i = start_pos; i < response.size(); ++i) {
        if (response[i] == '{') {
            brace_count++; // Increment for every '{'
        } else if (response[i] == '}') {
            brace_count--; // Decrement for every '}'
        }

        // If brace_count returns to zero, we found the complete JSON object
        if (brace_count == 0) {
            end_pos = i; // Set end_pos to the current position
            break; // Break out of the loop
        }
    }

    // If brace_count is not zero, it means there was an imbalance (unmatched braces)
    if (brace_count != 0) {
        return ""; // Return empty string if JSON is incomplete
    }

    // Extract and return the substring that represents the JSON object
    return response.substr(start_pos, end_pos - start_pos + 1);
}