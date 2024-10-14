#include <iostream>
#include <vector>
#include <string>
#include <algorithm> // For std::max

std::vector<int> calculate_column_widths(const std::vector<std::vector<std::string>>& data) {
    // Initialize a vector to hold the maximum widths for each column.
    // This assumes that all rows in data have the same number of columns.
    std::vector<int> widths(data[0].size(), 0);

    // Iterate over each row in the data.
    for (const auto& row : data) {
        // Iterate over each column in the row.
        for (size_t idx = 0; idx < row.size(); ++idx) {
            // Update the width at index `idx` with the maximum of the current width
            // and the length of the string in the current column.
            widths[idx] = std::max(widths[idx], static_cast<int>(row[idx].length()));
        }
    }

    // Return the vector of maximum widths for each column.
    return widths;
}

int main() {
    // Example usage
    std::vector<std::vector<std::string>> data = {{"apple", "banana"}, {"cherry", "date"}};
    std::vector<int> result = calculate_column_widths(data);
    
    // Output the results
    for (int width : result) {
        std::cout << width << " ";
    }
    std::cout << std::endl;

    return 0;
}