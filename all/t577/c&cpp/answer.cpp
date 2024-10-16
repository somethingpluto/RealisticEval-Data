#include <iostream>
#include <string>
#include <iomanip>

std::string formatPostCount(int count) {
    if (count == 0) {
        return "No Posts";
    } else {
        std::string postCount = std::to_string(count);
        postCount.insert(0, 2 - postCount.length(), '0'); // Ensure at least two digits
        std::string postWord = (count == 1) ? "Post" : "Posts"; // Singular or plural
        return postCount + " " + postWord; // Correctly formatted string
    }
}