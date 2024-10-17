#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <regex>
#include <algorithm>

// Function to count the occurrences of specified words in the given text
std::unordered_map<std::string, int> word_filter_counter(const std::string& text, const std::vector<std::string>& filter_words) {
    // Convert filter words to lowercase for case-insensitive comparison
    std::unordered_set<std::string> filter_words_set;
    for (const auto& word : filter_words) {
        std::string lower_word = word;
        std::transform(lower_word.begin(), lower_word.end(), lower_word.begin(), ::tolower);
        filter_words_set.insert(lower_word);
    }

    // Find all words in the text using a regex pattern
    std::regex word_pattern(R"(\b\w+(?:'\w+)?\b)");
    std::sregex_iterator words_begin = std::sregex_iterator(text.begin(), text.end(), word_pattern);
    std::sregex_iterator words_end = std::sregex_iterator();

    // Count occurrences of filtered words
    std::unordered_map<std::string, int> word_counts;
    for (std::sregex_iterator i = words_begin; i != words_end; ++i) {
        std::string word = (*i).str();
        std::transform(word.begin(), word.end(), word.begin(), ::tolower);
        if (filter_words_set.find(word) != filter_words_set.end()) {
            word_counts[word]++;
        }
    }

    // Create an ordered output based on the original order of filter_words
    std::unordered_map<std::string, int> ordered_output;
    for (const auto& word : filter_words) {
        std::string lower_word = word;
        std::transform(lower_word.begin(), lower_word.end(), lower_word.begin(), ::tolower);
        ordered_output[word] = word_counts[lower_word];
    }

    return ordered_output;
}