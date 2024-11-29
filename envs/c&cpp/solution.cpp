#include <iostream>
#include <string>
#include <vector>
#include <nlohmann/json.hpp>

using json = nlohmann::json;

// Function to sanitize a JSON object by removing specific keys.
json sanitize_data(const json& data, const std::set<std::string>* key_to_remove = nullptr) {
    static const std::set<std::string> default_keys_to_remove = {
        "email", "pc_conflicts", "metadata", "eligible_student_paper_prize", "talk_poster",
        "submitted_at", "decision", "status", "submitted", "submission"
    };

    const std::set<std::string>& keys_to_remove = (key_to_remove == nullptr) ? default_keys_to_remove : *key_to_remove;

    if (data.is_object()) {
        json sanitized;
        for (const auto& item : data.items()) {
            if (keys_to_remove.find(item.key()) == keys_to_remove.end()) {
                sanitized[item.key()] = sanitize_data(item.value());
            }
        }
        return sanitized;
    } else if (data.is_array()) {
        json sanitized;
        for (const auto& value : data) {
            sanitized.push_back(sanitize_data(value));
        }
        return sanitized;
    } else {
        return data;
    }
}