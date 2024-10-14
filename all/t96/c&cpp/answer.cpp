#include <string>

std::string changedClef(const std::string& abc, const std::string& clef = "bass") {
    size_t clef_index = abc.find("\nK:");

    // If the key signature is found
    if (clef_index != std::string::npos) {
        // Find the next newline character after the key signature line, or if none exists, use the end of the string
        size_t next_newline = abc.find("\n", clef_index + 1);
        if (next_newline == std::string::npos) {
            next_newline = abc.length();
        }

        // Create the string to inject, which includes the clef
        std::string injection = " clef=" + clef;

        // Construct the new ABC string with the injected clef
        return abc.substr(0, next_newline) + injection + abc.substr(next_newline);
    }

    // If the key signature is not found, return the original string
    return abc;
}