#include <iostream>
#include <vector>

std::vector<char> getAllAlphabets() {
    const int alphabetCount = 26; // Number of letters in the English alphabet
    std::vector<char> alphabets(alphabetCount * 2);
    
    for (int index = 0; index < alphabetCount * 2; ++index) {
        char charCode = index < alphabetCount ? 'a' + index : 'A' + (index - alphabetCount);
        alphabets[index] = charCode;
    }
    
    return alphabets;
}