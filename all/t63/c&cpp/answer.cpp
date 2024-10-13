#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>

// Assuming DataFrame is a custom class that provides similar functionality to pandas DataFrame
class DataFrame {
public:
    std::vector<std::vector<std::string>> data;
    std::vector<std::string> columns;

    // Constructor to initialize the DataFrame
    DataFrame(const std::vector<std::vector<std::string>>& data, const std::vector<std::string>& columns)
        : data(data), columns(columns) {}

    // Iterator for rows
    struct RowIterator {
        const std::vector<std::vector<std::string>>& data;
        size_t index;

        RowIterator(const std::vector<std::vector<std::string>>& data, size_t index)
            : data(data), index(index) {}

        bool operator!=(const RowIterator& other) const {
            return index != other.index;
        }

        void operator++() {
            ++index;
        }

        std::vector<std::string>& operator*() {
            return data[index];
        }
    };

    RowIterator begin() {
        return RowIterator(data, 0);
    }

    RowIterator end() {
        return RowIterator(data, data.size());
    }
};

std::string dataframe_to_markdown(const DataFrame& df, const std::string& md_path) {
    // Construct the header row
    std::stringstream headers;
    headers << "| ";
    for (size_t i = 0; i < df.columns.size(); ++i) {
        headers << df.columns[i];
        if (i < df.columns.size() - 1) {
            headers << " | ";
        }
    }
    headers << " |\n";

    // Construct the separator row
    std::stringstream separators;
    separators << "| ";
    for (size_t i = 0; i < df.columns.size(); ++i) {
        separators << "---";
        if (i < df.columns.size() - 1) {
            separators << " | ";
        }
    }
    separators << " |\n";

    // Combine headers and separators
    std::string markdown = headers.str() + separators.str();

    // Build markdown table body
    for (auto it = df.begin(); it != df.end(); ++it) {
        std::stringstream row;
        row << "| ";
        for (size_t i = 0; i < (*it).size(); ++i) {
            row << (*it)[i];
            if (i < (*it).size() - 1) {
                row << " | ";
            }
        }
        row << " |\n";
        markdown += row.str();
    }

    // Write markdown to file
    std::ofstream handle(md_path);
    if (handle.is_open()) {
        handle << markdown;
        handle.close();
    } else {
        std::cerr << "Failed to open file: " << md_path << std::endl;
    }

    return markdown;
}

int main() {
    // Example usage
    std::vector<std::vector<std::string>> data = {{"1", "2", "3"}, {"4", "5", "6"}};
    std::vector<std::string> columns = {"A", "B", "C"};
    DataFrame df(data, columns);

    std::string markdown = dataframe_to_markdown(df, "output.md");
    std::cout << markdown << std::endl;

    return 0;
}