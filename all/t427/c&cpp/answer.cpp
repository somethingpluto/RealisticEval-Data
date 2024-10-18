#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <map>
#include <sstream>

// Function to read sequences from a file and return them as a vector of vectors.
std::vector<std::vector<int>> read_sequences_from_file(const std::string& filename) {
    std::vector<std::vector<int>> sequences;
    std::ifstream file(filename);
    if (!file.is_open()) {
        std::cerr << "Error opening file: " << filename << std::endl;
        return sequences;
    }

    std::string line;
    while (std::getline(file, line)) {
        std::istringstream iss(line);
        std::vector<int> seq;
        std::string number;
        while (std::getline(iss, number, ',')) {
            seq.push_back(std::stoi(number));
        }
        sequences.push_back(seq);
    }
    file.close();
    return sequences;
}

// Function to check if the given sequence is a Munodi sequence (arithmetic progression).
bool is_munodi_sequence(const std::vector<int>& sequence) {
    if (sequence.size() < 2) {
        return false; // A sequence with less than 2 elements cannot be a Munodi sequence
    }

    int common_difference = sequence[1] - sequence[0];
    for (size_t i = 2; i < sequence.size(); ++i) {
        if (sequence[i] - sequence[i - 1] != common_difference) {
            return false; // Found a different difference, not a Munodi sequence
        }
    }
    return true; // All differences are the same
}

// Function to read sequences from a file and determine if each is a Munodi sequence.
std::map<std::vector<int>, bool> check_sequences(const std::string& filename) {
    std::vector<std::vector<int>> sequences = read_sequences_from_file(filename);
    std::map<std::vector<int>, bool> results;

    for (const auto& seq : sequences) {
        results[seq] = is_munodi_sequence(seq);
    }
    return results;
}
