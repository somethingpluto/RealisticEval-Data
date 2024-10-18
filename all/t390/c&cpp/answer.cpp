#include <iostream>
#include <string>
#include <vector>
#include <regex>
#include <stdexcept>

std::vector<std::string> split_into_sentences(const std::string& text) {
    /**
     * Split the input text string into sentences.
     *
     * Args:
     *     text (const std::string&): The input text to be split into sentences.
     *
     * Returns:
     *     std::vector<std::string>: A vector of sentences extracted from the input text, cleaned and stripped of leading/trailing whitespace.
     */

    // Check if the input is a string (in C++, this is always true since it's a function parameter)
    if (text.empty()) {
        throw std::invalid_argument("Input must be a non-empty string.");
    }

    // Regular expression to split the text where there is a punctuation followed by space or end of string
    // This handles situations where punctuation might be followed by a quotation mark or other punctuation
    std::regex sentence_delimiters(R"((?<=[.!?]["”’])\s+(?=[A-Z]))");

    // Split the text using the defined regular expression
    std::sregex_token_iterator iter(text.begin(), text.end(), sentence_delimiters, -1);
    std::sregex_token_iterator end;

    std::vector<std::string> sentences;
    for (; iter != end; ++iter) {
        std::string sentence = *iter;
        // Remove any leading or trailing whitespace from each sentence
        auto start = sentence.find_first_not_of(" \t\n\r\f\v");
        auto end = sentence.find_last_not_of(" \t\n\r\f\v");
        if (start != std::string::npos) {
            sentences.push_back(sentence.substr(start, (end - start + 1)));
        }
    }

    // Return the cleaned list of sentences
    return sentences;
}
