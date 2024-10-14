TEST_CASE("TestSanitizeFilename", "[sanitize_filename]") {
    SECTION("test_valid_filename") {
        REQUIRE(sanitize_filename("valid_filename.txt") == "valid_filename.txt");
    }

    SECTION("test_illegal_characters") {
        REQUIRE(sanitize_filename("invalid<filename>.txt") == "invalid_filename_.txt");
        REQUIRE(sanitize_filename("file/name:with*illegal|chars?.txt") == "file_name_with_illegal_chars_.txt");
    }

    SECTION("test_long_filename") {
        std::string long_filename = std::string(300, 'a') + ".txt";
        std::string sanitized_filename = sanitize_filename(long_filename);
        REQUIRE(sanitized_filename.length() == 255);
        REQUIRE(sanitized_filename == std::string(255, 'a'));
    }

    SECTION("test_empty_filename") {
        REQUIRE(sanitize_filename("") == "");
    }
}
