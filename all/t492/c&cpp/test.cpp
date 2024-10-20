TEST_CASE("TestSaveContentToFile", "[save_content_to_file]") {
    const std::string test_file_path = "test_output.txt";

    SECTION("Basic content") {
        std::string content = "Hello,  World!  ";
        std::string expected = "Hello, World!";
        save_content_to_file(content, test_file_path);

        std::ifstream file(test_file_path);
        REQUIRE(file.is_open());
        std::string result((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());
        file.close();

        REQUIRE(result == expected);
    }

    SECTION("Multiple spaces and empty lines") {
        std::string content = R"(
        
        This is a    test.

        Another line.      
        )";
        std::string expected = "This is a test. Another line.";
        save_content_to_file(content, test_file_path);

        std::ifstream file(test_file_path);
        REQUIRE(file.is_open());
        std::string result((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());
        file.close();

        REQUIRE(result == expected);
    }

    SECTION("Only whitespace") {
        std::string content = "    \n  \n   ";
        std::string expected = "";
        save_content_to_file(content, test_file_path);

        std::ifstream file(test_file_path);
        REQUIRE(file.is_open());
        std::string result((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());
        file.close();

        REQUIRE(result == expected);
    }

    SECTION("Empty content") {
        std::string content = "";
        std::string expected = "";
        save_content_to_file(content, test_file_path);

        std::ifstream file(test_file_path);
        REQUIRE(file.is_open());
        std::string result((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());
        file.close();

        REQUIRE(result == expected);
    }

    // Clean up the test file after all sections
    if (fs::exists(test_file_path)) {
        fs::remove(test_file_path);
    }
}