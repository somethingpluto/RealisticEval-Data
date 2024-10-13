#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <set>

// Function to check for ticker symbols with the same ex-dividend date but different dividend amounts
std::vector<std::pair<std::string, std::string>> checkDividendVariances(const std::vector<std::tuple<std::string, std::string, int>>& records) {
    // Dictionary to store dividend amounts by (ticker, ex_dividend_date)
    std::unordered_map<std::pair<std::string, std::string>, std::set<int>> dividendDict;

    // Iterate through the records
    for (const auto& record : records) {
        const std::string& ticker = std::get<0>(record);
        const std::string& exDividendDate = std::get<1>(record);
        int dividendAmount = std::get<2>(record);

        std::pair<std::string, std::string> key(ticker, exDividendDate);
        dividendDict[key].insert(dividendAmount);
    }

    // Find entries with more than one unique dividend amount
    std::vector<std::pair<std::string, std::string>> result;
    for (const auto& entry : dividendDict) {
        if (entry.second.size() > 1) {
            result.push_back(entry.first);
        }
    }

    return result;
}

int main() {
    // Example usage
    std::vector<std::tuple<std::string, std::string, int>> records = {
        {"AAPL", "2023-06-01", 100},
        {"AAPL", "2023-06-01", 150},
        {"GOOGL", "2023-06-01", 200},
        {"MSFT", "2023-06-01", 120},
        {"AAPL", "2023-06-02", 100}
    };

    auto result = checkDividendVariances(records);

    // Print the result
    for (const auto& entry : result) {
        std::cout << "(" << entry.first << ", " << entry.second << ")" << std::endl;
    }

    return 0;
}