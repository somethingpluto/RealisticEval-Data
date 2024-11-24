#include <iostream>
#include <sstream>
#include <string>
#include <vector>

// Function to split a string by newline character
std::vector<std::string> split(const std::string &s, char delimiter) {
    std::vector<std::string> tokens;
    std::string token;
    std::istringstream tokenStream(s);
    while (std::getline(tokenStream, token, delimiter)) {
        tokens.push_back(token);
    }
    return tokens;
}

// Class to wrap text content
class TextWrapper {
public:
    // Constructor with optional width parameter
    explicit TextWrapper(int width = 80) : m_width(width) {}

    // Generator function to wrap and yield lines
    class LineGenerator {
    private:
        std::string m_line;
        int m_width;
        std::istringstream m_stream;

    public:
        // Constructor for LineGenerator
        LineGenerator(const std::string &line, int width)
            : m_line(line), m_width(width), m_stream(line) {}

        // Generate and yield wrapped lines
        bool next(std::string &wrappedLine) {
            std::string temp;
            std::string currentLine;
            while (m_stream >> temp) {
                if (currentLine.length() + temp.length() + 1 > m_width) {
                    wrappedLine = currentLine;
                    currentLine.clear();
                    if (!temp.empty()) {
                        m_stream.unget(); // Put back the last word to process it in the next iteration
                    }
                    return true;
                }
                if (!currentLine.empty())
                    currentLine += " ";
                currentLine += temp;
            }
            if (!currentLine.empty()) {
                wrappedLine = currentLine;
                return true;
            }
            return false;
        }
    };

    // Function to wrap and yield lines from the input content
    void wrapContent(const std::string &content, std::function<void(const std::string&)> callback) {
        auto lines = split(content, '\n');
        for (const auto &line : lines) {
            if (line.find_first_not_of(" \t") == std::string::npos) {  // Check if the line is essentially empty.
                callback("\n");
            } else {
                LineGenerator generator(line, m_width);
                std::string wrappedLine;
                while (generator.next(wrappedLine)) {
                    callback(wrappedLine);
                }
            }
        }
    }

private:
    int m_width;
};

// Function to wrap the text content to the specified maximum width and generate these lines line by line
void wrap_content_generator(const std::string &content, int width = 80, std::function<void(const std::string&)> callback) {
    /*
     * Wrap the text content to the specified maximum width and generate these lines line by line
     *
     * Args:
     *     content (std::string): The content to be wrapped and yielded line by line.
     *     width (int): The maximum width of the lines, default is 80 characters.
     *
     * Yields:
     *     std::string: Each line of the content wrapped to the specified width.
     */

    // Split the content into lines
    auto lines = split(content, '\n');

    for (const auto &line : lines) {
        if (line.find_first_not_of(" \t") == std::string::npos) {  // Check if the line is essentially empty.
            callback("\n");
        } else {
            std::istringstream iss(line);
            std::string word;
            std::string currentLine;
            while (iss >> word) {
                if (currentLine.length() + word.length() + 1 > width) {
                    callback(currentLine);
                    currentLine = word;
                } else {
                    if (!currentLine.empty())
                        currentLine += " ";
                    currentLine += word;
                }
            }
            if (!currentLine.empty()) {
                callback(currentLine);
            }
        }
    }
}