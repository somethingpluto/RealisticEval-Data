#include <iostream>
#include <sstream>
#include <string>

int countWords(const std::string &str) {
    // Initialize a word count variable
    int wordCount = 0;
    std::istringstream stream(str); // Create a string stream from the input string
    std::string word; // Variable to hold each word

    // Extract words from the stream
    while (stream >> word) {
        wordCount++; // Increment the count for each word found
    }

    return wordCount; // Return the total word count
}