#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>

std::string csvToSQLInsert(const std::string& csvFilePath) {
    std::ifstream csvFile(csvFilePath);
    if (!csvFile.is_open()) {
        return "Error opening file";
    }

    std::string line;
    std::getline(csvFile, line); // Read the header line
    std::istringstream ss(line);
    std::vector<std::string> headers((std::istream_iterator<std::string>(ss)),
                                     std::istream_iterator<std::string>());

    std::string tableName = csvFilePath.substr(0, csvFilePath.find_last_of('.'));
    std::string sqlStatements;

    while (std::getline(csvFile, line)) {
        ss.clear();
        ss.str(line);
        std::vector<std::string> values((std::istream_iterator<std::string>(ss)),
                                        std::istream_iterator<std::string>());

        if (values.size() != headers.size()) {
            continue; // Skip rows with incorrect number of columns
        }

        sqlStatements += "INSERT INTO " + tableName + "(";
        for (size_t i = 0; i < headers.size(); ++i) {
            sqlStatements += headers[i];
            if (i < headers.size() - 1) {
                sqlStatements += ", ";
            }
        }
        sqlStatements += ") VALUES (";

        for (size_t i = 0; i < values.size(); ++i) {
            if (values[i].find_first_not_of("0123456789.-") == std::string::npos) {
                sqlStatements += "'" + values[i] + "'";
            } else {
                sqlStatements += values[i];
            }
            if (i < values.size() - 1) {
                sqlStatements += ", ";
            }
        }
        sqlStatements += ");\n";
    }

    csvFile.close();
    return sqlStatements;
}