TEST_CASE_METHOD(TestAnswer, "Test processing of normal input") {
    write_to_file("Line 1\nLine 2 # Comment\nLine 3\n");
    auto result = read_file_and_process_lines(test_file_path);
    REQUIRE(result == std::vector<std::string>{"Line 1", "Line 2", "Line 3"});
}

TEST_CASE_METHOD(TestAnswer, "Test processing when only comments are present") {
    write_to_file("# This is a comment\n# Another comment\n");
    auto result = read_file_and_process_lines(test_file_path);
    REQUIRE(result.empty());
}

TEST_CASE_METHOD(TestAnswer, "Test processing with empty lines") {
    write_to_file("Line 1\n\nLine 2\n\n\nLine 3 # Comment\n");
    auto result = read_file_and_process_lines(test_file_path);
    REQUIRE(result == std::vector<std::string>{"Line 1", "Line 2", "Line 3"});
}

TEST_CASE_METHOD(TestAnswer, "Test processing when there are no inline comments") {
    write_to_file("Line 1\nLine 2\nLine 3\n");
    auto result = read_file_and_process_lines(test_file_path);
    REQUIRE(result == std::vector<std::string>{"Line 1", "Line 2", "Line 3"});
}

TEST_CASE_METHOD(TestAnswer, "Test processing with only new lines") {
    write_to_file("\n\n\n\n");
    auto result = read_file_and_process_lines(test_file_path);
    REQUIRE(result.empty());
}

TEST_CASE_METHOD(TestAnswer, "Test processing with mixed content") {
    write_to_file("Valid line\n# This is a comment\nLine 2\n# Another comment\n\nLine 3 # End of line comment\n");
    auto result = read_file_and_process_lines(test_file_path);
    REQUIRE(result == std::vector<std::string>{"Valid line", "Line 2", "Line 3"});
}