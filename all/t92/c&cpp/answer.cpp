#include <iostream>
#include <string>
#include <unordered_map>

std::string replaceHtmlEntities(const std::string& htmlString) {
    if (htmlString.empty()) {
        throw std::invalid_argument("Input must be a non-empty string.");
    }

    std::unordered_map<std::string, char> entities = {
        {"&lt;", '<'}, {"&gt;", '>'}, {"&amp;", '&'},
        {"&quot;", '\"'}, {"&apos;", '\''}
    };

    std::string decodedString;
    std::string currentEntity;

    for (size_t i = 0; i < htmlString.length(); ++i) {
        if (htmlString[i] == '&') {
            currentEntity.clear();
            while (i < htmlString.length() && htmlString[i] != ';') {
                currentEntity += htmlString[i++];
            }
            currentEntity += ';';  // Add the semicolon
            if (entities.count(currentEntity)) {
                decodedString += entities[currentEntity];
            } else {
                decodedString += currentEntity;  // Add as is if not found
            }
        } else {
            decodedString += htmlString[i];
        }
    }

    return decodedString;
}