#include <iostream>
#include <fstream>
#include <string>
#include <map>

void extract_log_entries(const std::string& log_file_path) {
    // Define log level keywords
    const std::map<std::string, std::string> log_levels = {
        {"WARNING", "warnings.log"},
        {"ERROR", "errors.log"},
        {"CRITICAL", "criticals.log"},
        {"ALERT", "alerts.log"}
    };

    // Open the input log file
    std::ifstream log_file(log_file_path);
    if (!log_file.is_open()) {
        std::cerr << "Failed to open log file: " << log_file_path << std::endl;
        return;
    }

    // Process each line in the log file
    std::string line;
    while (std::getline(log_file, line)) {
        for (const auto& [level, filename] : log_levels) {
            if (line.find(level) != std::string::npos) {
                // Open the output file for appending
                std::ofstream out_file(filename, std::ios::app);
                if (out_file.is_open()) {
                    out_file << line << std::endl;
                    out_file.close();
                } else {
                    std::cerr << "Failed to open output file: " << filename << std::endl;
                }
                break; // Move to next line after writing to one file
            }
        }
    }

    log_file.close();
}