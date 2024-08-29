TEST_CASE("getLastPartOfFilepath Test Cases", "[getLastPartOfFilepath]") {
    // Test Case 1: Typical Unix file path with '/'
    REQUIRE(getLastPartOfFilepath("/home/user/documents/report.txt", '/') == "report.txt");

    // Test Case 2: Typical Windows file path with '\\'
    REQUIRE(getLastPartOfFilepath("C:\\Users\\JohnDoe\\Desktop\\image.png", '\\') == "image.png");

    // Test Case 3: No separator in the path, return the original string
    REQUIRE(getLastPartOfFilepath("filename.txt", '/') == "filename.txt");

    // Test Case 4: File path with trailing separator
    REQUIRE(getLastPartOfFilepath("/home/user/documents/", '/') == "");

    // Test Case 5: Empty string as input
    REQUIRE(getLastPartOfFilepath("", '/') == "");
}