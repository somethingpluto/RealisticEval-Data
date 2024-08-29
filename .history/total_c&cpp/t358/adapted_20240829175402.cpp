#include <vector>
#include <string>
#include <algorithm>
#include <cctype>

using namespace std;

/**
 * @brief Extracts the name and number from a string in the format "name + number".
 *
 * This helper function splits the input string into its name and number components.
 * It assumes that the string is well-formed, with the name part consisting of alphabetic characters
 * and the number part consisting of numeric digits.
 *
 * @param s The input string in the format "name + number".
 * @return A pair containing the name and number as a string and an integer, respectively.
 */
pair<string, int> extractNameAndNumber(const string& s) {
    int pos = s.size() - 1;
    while (pos >= 0 && isdigit(s[pos])) {
        pos--;
    }
    string name = s.substr(0, pos + 1);
    int number = stoi(s.substr(pos + 1));
    return {name, number};
}

/**
 * @brief Sort the string array with the shape of "name + number" in ascending order. If the numbers are the same, sort by name in ascending order, and return the sorted array
 *
 * This function sorts a vector of strings where each string is in the format "name + number".
 * Sorting is first done by the numeric part in ascending order, and if two strings have the same
 * numeric part, they are further sorted by the name part in ascending order.
 *
 * @param arr A reference to the vector of strings to be sorted.
 * @return A vector of strings sorted according to the rules described above.
 */
vector<string> sortStringArray(vector<string>& arr) {
    sort(arr.begin(), arr.end(), [](const string& a, const string& b) {
        auto [nameA, numberA] = extractNameAndNumber(a);
        auto [nameB, numberB] = extractNameAndNumber(b);
        if (numberA != numberB) {
            return numberA < numberB;
        }
        return nameA < nameB;
    });
    return arr;
}