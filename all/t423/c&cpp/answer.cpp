#include <iostream>
#include <fstream>
#include <string>

void writeUniqueLineToFile(const std::string& filename, const std::string& lineContent) {
    /**
     * Writes a line to a text file only if the line with the same content does not already exist.
     *
     * Args:
     *      filename (std::string): The name of the file to write to.
     *      lineContent (std::string): The content of the line to write.
     *
     * Returns:
     *      None
     */
    // Check if the lineContent already exists in the file
    std::ifstream file(filename);
    if (file.is_open()) {
        std::string existingLine;
        while (getline(file, existingLine)) {
            if (existingLine == lineContent) {
                std::cout << "Line '" << lineContent << "' already exists in '" << filename << "'. Not writing again." << std::endl;
                file.close();
                return;
            }
        }
        file.close();
    } else {
        std::cerr << "Unable to open file: " << filename << std::endl;
        return;
    }

    // If lineContent is not found, append it to the file
    std::ofstream outFile(filename, std::ios_base::app); // Open file in append mode
    if (outFile.is_open()) {
        outFile << lineContent << '\n';
        outFile.close();
        std::cout << "Line '" << lineContent << "' successfully written to '" << filename << "'." << std::endl;
    } else {
        std::cerr << "Unable to open file: " << filename << std::endl;
    }
}
