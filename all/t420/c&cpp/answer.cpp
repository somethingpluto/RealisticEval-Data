#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <limits>
#include <algorithm>

// Read the file and convert each line into a vector of strings.
std::vector<std::vector<std::string>> read_file_as_sequences(const std::string& file_path) {
    std::ifstream file(file_path);
    std::vector<std::vector<std::string>> sequences;
    std::string line;

    while (std::getline(file, line)) {
        std::istringstream iss(line);
        std::vector<std::string> words;
        std::string word;
        while (iss >> word) {
            words.push_back(word);
        }
        sequences.push_back(words);
    }

    return sequences;
}

// Find the indices of two words in a sequence and calculate their closest distances.
int find_closest_word_indices(const std::vector<std::string>& sequence, const std::string& word1, const std::string& word2) {
    std::vector<int> word1_indices;
    std::vector<int> word2_indices;
    int min_distance = std::numeric_limits<int>::max();

    // Gather indices for both words
    for (size_t index = 0; index < sequence.size(); ++index) {
        if (sequence[index] == word1) {
            word1_indices.push_back(index);
        } else if (sequence[index] == word2) {
            word2_indices.push_back(index);
        }
    }

    // Calculate the minimum distance between all pairs of indices
    for (int index1 : word1_indices) {
        for (int index2 : word2_indices) {
            int distance = std::abs(index1 - index2);
            if (distance < min_distance) {
                min_distance = distance;
            }
        }
    }

    return min_distance;
}

// Determine the minimum distance between two words in any line of a file.
std::pair<int, int> get_min_distance(const std::string& file_path, const std::string& word1, const std::string& word2) {
    auto sequences = read_file_as_sequences(file_path);
    int min_distance = std::numeric_limits<int>::max();
    int min_seq_num = -1;

    for (size_t i = 0; i < sequences.size(); ++i) {
        int distance = find_closest_word_indices(sequences[i], word1, word2);
        if (distance < min_distance) {
            min_distance = distance;
            min_seq_num = static_cast<int>(i);
        }
    }

    if (min_distance == std::numeric_limits<int>::max()) {
        return std::make_pair(-1, -1);
    } else {
        return std::make_pair(min_seq_num, min_distance);
    }
}