TEST_CASE("Test replace_words_in_file") {
    SECTION("test_replace_single_word") {
        const std::string file_path = "dummy_path.txt";
        const std::unordered_map<std::string, std::string> replacement_dict = {{"hello", "hi"}};
        const std::string expected_output = "hi world";

        // Mock file content
        std::istringstream mock_file_content("hello world");

        // Redirect file stream to mock file content
        std::istringstream original_cin(std::cin.rdbuf());
        std::cin.rdbuf(mock_file_content.rdbuf());

        std::string result = replaceWordsInFile(file_path, replacement_dict);

        // Restore original file stream
        std::cin.rdbuf(original_cin.rdbuf());

        REQUIRE(result == expected_output);
    }

    SECTION("test_replace_multiple_words") {
        const std::string file_path = "dummy_path.txt";
        const std::unordered_map<std::string, std::string> replacement_dict = {{"hello", "hi"}, {"world", "earth"}};
        const std::string expected_output = "hi earth";

        // Mock file content
        std::istringstream mock_file_content("hello world");

        // Redirect file stream to mock file content
        std::istringstream original_cin(std::cin.rdbuf());
        std::cin.rdbuf(mock_file_content.rdbuf());

        std::string result = replaceWordsInFile(file_path, replacement_dict);

        // Restore original file stream
        std::cin.rdbuf(original_cin.rdbuf());

        REQUIRE(result == expected_output);
    }

    SECTION("test_no_replacement") {
        const std::string file_path = "dummy_path.txt";
        const std::unordered_map<std::string, std::string> replacement_dict = {{"goodbye", "bye"}};
        const std::string expected_output = "hello world";

        // Mock file content
        std::istringstream mock_file_content("hello world");

        // Redirect file stream to mock file content
        std::istringstream original_cin(std::cin.rdbuf());
        std::cin.rdbuf(mock_file_content.rdbuf());

        std::string result = replaceWordsInFile(file_path, replacement_dict);

        // Restore original file stream
        std::cin.rdbuf(original_cin.rdbuf());

        REQUIRE(result == expected_output);
    }

    SECTION("test_empty_file") {
        const std::string file_path = "dummy_path.txt";
        const std::unordered_map<std::string, std::string> replacement_dict = {{"hello", "hi"}};
        const std::string expected_output = "";

        // Mock file content
        std::istringstream mock_file_content("");

        // Redirect file stream to mock file content
        std::istringstream original_cin(std::cin.rdbuf());
        std::cin.rdbuf(mock_file_content.rdbuf());

        std::string result = replaceWordsInFile(file_path, replacement_dict);

        // Restore original file stream
        std::cin.rdbuf(original_cin.rdbuf());

        REQUIRE(result == expected_output);
    }
}