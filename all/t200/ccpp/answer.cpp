#include <iostream>
#include <vector>
#include <functional>
#include <fstream>
#include <ctime>
#include <string>

string token_manager::extract_json(const std::string& input)
{
    std::string result;
    int bracket_count = 0;
    size_t start_pos = std::string::npos;
    size_t end_pos = std::string::npos;

    for (size_t i = 0; i < input.length(); ++i) {
        if (input[i] == '{') {
            if (bracket_count == 0) {
                start_pos = i;  // 记录第一个 '{' 的位置
            }
            bracket_count++;
        } else if (input[i] == '}') {
            bracket_count--;
            if (bracket_count == 0) {
                end_pos = i;  // 记录匹配的 '}' 的位置
                break;
            }
        }
    }

    if (start_pos != std::string::npos && end_pos != std::string::npos) {
        result = input.substr(start_pos, end_pos - start_pos + 1);
    }

    return result;
}
