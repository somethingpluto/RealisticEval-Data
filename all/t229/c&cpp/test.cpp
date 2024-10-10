TEST_CASE("Convert file size to human-readable format", "[convert_file_size]") {
    REQUIRE(convert_file_size(2120) == "2KB");
    REQUIRE(convert_file_size(1048576) == "1MB");
    REQUIRE(convert_file_size(1073741824) == "1GB");
    // Add more test cases as needed
}