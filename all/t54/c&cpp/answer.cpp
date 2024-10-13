#include <iostream>
#include <vector>
#include <string>

// Function to remove all occurrences of three consecutive backticks from each string in the list
std::vector<std::string> remove_triple_backticks(const std::vector<std::string>& string_list) {
    std::vector<std::string> processed_list;
    for (const auto& s : string_list) {
        std::string processed_string = s;
        size_t pos = 0;
        // Find and replace all occurrences of '```' with an empty string
        while ((pos = processed_string.find("```", pos)) != std::string::npos) {
            processed_string.erase(pos, 3);
        }
        processed_list.push_back(processed_string);
    }
    return processed_list;
}

int main() {
    // Example usage
    std::vector<std::string> string_list = {"Hello ``` World", "This is a test ```", "No backticks here"};
    std::vector<std::string> result = remove_triple_backticks(string_list);

    // Output the results
    for (const auto& s : result) {
        std::cout << s << std::endl;
    }

    return 0;
}