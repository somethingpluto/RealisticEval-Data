#include <iostream>
#include <filesystem>

void emptyDirectory(const std::string &directoryPath) {
    try {
        for(auto &entry : std::filesystem::directory_iterator(directoryPath)) {
            if(entry.is_regular_file()) {
                std::filesystem::remove(entry.path());
            } else if(entry.is_directory()) {
                emptyDirectory(entry.path().string()); // Recursive call
                std::filesystem::remove_all(entry.path());
            }
        }
    } catch(std::filesystem::filesystem_error &e) {
        std::cerr << "Error occurred while processing directory: " << e.what() << '\n';
    }
}