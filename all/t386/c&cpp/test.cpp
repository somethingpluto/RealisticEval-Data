TEST_CASE("Test Fix Encoding", "[encoding]") {
    // Create a directory for test files if it doesn't exist
    const std::string test_dir = "test_files";
    fs::create_directories(test_dir);

    const std::string input_file_path = fs::path(test_dir) / "test_input.txt";
    const std::string output_file_path = fs::path(test_dir) / "test_output.txt";

    auto write_to_file = [&] (const std::string& file_path, const std::string& text, const std::string& encoding) {
        // Helper method to write text to a file with a specific encoding
        std::ofstream file(file_path, std::ios::binary);
        file << text;
    };

    SECTION("Basic Conversion") {
        // Test basic conversion from cp932 to utf_16
        write_to_file(input_file_path, "これはテストです", "cp932");
        bool result = convert_encoding(input_file_path, output_file_path);
        REQUIRE(result);

        std::ifstream output_file(output_file_path, std::ios::binary);
        REQUIRE(output_file.is_open());
        std::stringstream buffer;
        buffer << output_file.rdbuf();
        std::string content = buffer.str();
        REQUIRE(content == "これはテストです");
    }

    SECTION("No Conversion Needed") {
        // Test when no conversion is needed because file is already in target encoding
        write_to_file(input_file_path, "No conversion needed", "utf_16");
        bool result = convert_encoding(input_file_path, output_file_path, "utf_16");
        REQUIRE(result);

        std::ifstream output_file(output_file_path, std::ios::binary);
        REQUIRE(output_file.is_open());
        std::stringstream buffer;
        buffer << output_file.rdbuf();
        std::string content = buffer.str();
        REQUIRE(content == "No conversion needed");
    }

    SECTION("Output Already Converted") {
        // Test behavior when file is already in target encoding and copied directly
        write_to_file(input_file_path, "Already utf_16", "utf_16");
        bool result = convert_encoding(input_file_path, output_file_path, "cp932", "utf_16");
        REQUIRE(result);

        std::ifstream output_file(output_file_path, std::ios::binary);
        REQUIRE(output_file.is_open());
        std::stringstream buffer;
        buffer << output_file.rdbuf();
        std::string content = buffer.str();
        REQUIRE(content == "Already utf_16");
    }

    // Clean up test directory and all created files after each test
    fs::remove_all(test_dir);
}