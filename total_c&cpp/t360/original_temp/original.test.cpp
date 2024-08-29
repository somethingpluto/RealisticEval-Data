#define CATCH_CONFIG_MAIN
#include "../../lib/catch.hpp"
#include "../original.cpp"
TEST_CASE("getLastPartOfFilepath Test Cases", "[getLastPartOfFilepath]") {
    // Test Case 1: Unix-style path with '/'
    REQUIRE(getLastPartOfFilepath("/home/user/documents/file.txt") == "file.txt");

    // Test Case 2: Windows-style path with '\\'
    REQUIRE(getLastPartOfFilepath("C:\\Users\\JohnDoe\\Documents\\file.txt") == "file.txt");

    // Test Case 3: Path without any separators (should return the original string)
    REQUIRE(getLastPartOfFilepath("file.txt") == "file.txt");

    // Test Case 4: Path ending with a separator (should return an empty string)
    REQUIRE(getLastPartOfFilepath("/home/user/documents/") == "");

    // Test Case 5: Path with mixed separators (should return the last part after the last separator)
    REQUIRE(getLastPartOfFilepath("C:/Users\\JohnDoe/Documents/file.txt") == "file.txt");
}