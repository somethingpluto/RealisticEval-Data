#include <iostream>
#include <string>
#include <stack>
#include <unordered_map>

// Function to extract the contents of the outermost brackets from the input string
std::string extract_outermost_brackets(const std::string& s) {
    std::stack<char> stack;
    int start_index = -1;
    std::unordered_map<char, char> opening_brackets = {{'(', '('}, {'{', '{'}, {'[', '['}};
    std::unordered_map<char, char> closing_brackets = {{')', '('}, {'}', '{'}, {']', '['}};
    std::unordered_map<char, char> matching_bracket = {{')', '('}, {'}', '{'}, {']', '['}};

    for (size_t i = 0; i < s.size(); ++i) {
        char char_current = s[i];
        if (opening_brackets.find(char_current) != opening_brackets.end()) {
            if (stack.empty()) {
                start_index = static_cast<int>(i);
            }
            stack.push(char_current);
        } else if (closing_brackets.find(char_current) != closing_brackets.end()) {
            if (!stack.empty() && stack.top() == matching_bracket[char_current]) {
                stack.pop();
                if (stack.empty()) {
                    return s.substr(start_index + 1, i - start_index - 1);
                }
            }
        }
    }

    return "";  // Return an empty string if no outermost brackets were found
}
