#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <nlohmann/json.hpp>

using json = nlohmann::json;

std::pair<std::vector<double>, std::vector<double>> read_log(const std::string &log_file_path) {
    std::ifstream logFile(log_file_path);
    if (!logFile.is_open()) {
        throw std::runtime_error("Failed to open log file");
    }

    std::vector<double> train_loss_list;
    std::vector<double> test_acc1_list;

    std::string line;
    while (getline(logFile, line)) {
        try {
            json j = json::parse(line);
            train_loss_list.push_back(j["train_loss"]);
            test_acc1_list.push_back(j["test_acc1"]);
        } catch (...) {
            // If parsing fails, skip this line
        }
    }

    return {train_loss_list, test_acc1_list};
}