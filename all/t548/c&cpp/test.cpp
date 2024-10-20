TEST_CASE("Test read_txt_add_json_bracket") {
    SECTION("Valid JSON") {
        std::istringstream fake_file_stream(R"({"key": "value"})");
        std::string fake_filename = "fakefile.txt";

        // Mock the file stream
        std::ifstream::mock_file_stream::register_mock(fake_filename, fake_file_stream);

        auto result = read_txt_add_json_bracket(fake_filename);
        REQUIRE(result.size() == 1);
        REQUIRE(result[0] == json({{"key", "value"}}));
    }

    SECTION("Empty JSON Array") {
        std::istringstream fake_file_stream(R"([])");
        std::string fake_filename = "fakefile.txt";

        // Mock the file stream
        std::ifstream::mock_file_stream::register_mock(fake_filename, fake_file_stream);

        auto result = read_txt_add_json_bracket(fake_filename);
        REQUIRE(result.empty());
    }

    SECTION("Valid JSON with newline") {
        std::istringstream fake_file_stream(R"({"key": "value"}\n)");
        std::string fake_filename = "fakefile.txt";

        // Mock the file stream
        std::ifstream::mock_file_stream::register_mock(fake_filename, fake_file_stream);

        auto result = read_txt_add_json_bracket(fake_filename);
        REQUIRE(result.size() == 1);
        REQUIRE(result[0] == json({{"key", "value"}}));
    }

    SECTION("JSON with array") {
        std::istringstream fake_file_stream(R"({"key": "value"})");
        std::string fake_filename = "fakefile.txt";

        // Mock the file stream
        std::ifstream::mock_file_stream::register_mock(fake_filename, fake_file_stream);

        auto result = read_txt_add_json_bracket(fake_filename);
        REQUIRE(result.size() == 1);
        REQUIRE(result[0] == json({{"key", "value"}}));
    }
}