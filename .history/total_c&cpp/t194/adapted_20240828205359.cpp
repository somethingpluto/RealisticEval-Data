/**
 * @brief Returns a dynamically allocated copy of the specified string.
 *
 * This function creates a copy of the input string by allocating memory on the heap
 * and copying the content of the input string to the newly allocated memory. The caller
 * is responsible for freeing the allocated memory using `delete[]`.
 *
 * @param str The input C-string to be copied.
 * @return A pointer to the dynamically allocated copy of the input string.
 * @throws std::invalid_argument if the input string is null.
 */
char* copyString(const char* str) {
    if (str == nullptr) {
        throw std::invalid_argument("Input string cannot be null.");
    }

    // Allocate memory for the copy, including space for the null terminator
    char* copiedStr = new char[std::strlen(str) + 1];

    // Copy the string into the allocated memory
    std::strcpy(copiedStr, str);

    return copiedStr;
}