TEST_CASE("ExtractFileName Test Cases", "[extractFileName]") {
    // Test Case 1: Typical Unix file path with '/'
    REQUIRE(extractFileName("/home/user/documents/report.txt", '/') == "report.txt");

    // Test Case 2: Typical Windows file path with '\\'
    REQUIRE(extractFileName("C:\\Users\\JohnDoe\\Desktop\\image.png", '\\') == "image.png");

    // Test Case 3: No separator in the path, return the original string
    REQUIRE(extractFileName("filename.txt", '/') == "filename.txt");

    // Test Case 4: File path with trailing separator
    REQUIRE(extractFileName("/home/user/documents/", '/') == "");

    // Test Case 5: Empty string as input
    REQUIRE(extractFileName("", '/') == "");
}