TEST_CASE("Testformat_text", "[format_text]") {
    SECTION("test_basic_text") {
        // Test with basic text
        std::string input_text = "This is line one.\nThis is line two.\nThis is line three.";
        std::string expected_output = "This is line one. This is line two. This is line three.";

        // Create a temporary directory
        std::filesystem::path temp_dir = std::filesystem::temp_directory_path();
        std::string input_file_path = (temp_dir / "input.txt").string();
        std::string output_file_path = (temp_dir / "output.txt").string();

        // Write input text to the temporary input file
        std::ofstream input_file(input_file_path);
        input_file << input_text;
        input_file.close();

        // Call the format_text function
        format_text(input_file_path, output_file_path);

        // Read the output file
        std::ifstream output_file(output_file_path);
        std::string output_text((std::istreambuf_iterator<char>(output_file)), std::istreambuf_iterator<char>());
        output_file.close();

        // Check the output
        REQUIRE(expected_output == output_text);

        // Clean up
        std::remove(input_file_path.c_str());
        std::remove(output_file_path.c_str());
    }

    SECTION("test_single_line") {
        // Test with a single line
        std::string input_text = "This is a single line.";
        std::string expected_output = "This is a single line.";

        // Create a temporary directory
        std::filesystem::path temp_dir = std::filesystem::temp_directory_path();
        std::string input_file_path = (temp_dir / "input.txt").string();
        std::string output_file_path = (temp_dir / "output.txt").string();

        // Write input text to the temporary input file
        std::ofstream input_file(input_file_path);
        input_file << input_text;
        input_file.close();

        // Call the format_text function
        format_text(input_file_path, output_file_path);

        // Read the output file
        std::ifstream output_file(output_file_path);
        std::string output_text((std::istreambuf_iterator<char>(output_file)), std::istreambuf_iterator<char>());
        output_file.close();

        // Check the output
        REQUIRE(expected_output == output_text);

        // Clean up
        std::remove(input_file_path.c_str());
        std::remove(output_file_path.c_str());
    }

    SECTION("test_empty_file") {
        // Test with an empty file
        std::string input_text = "";
        std::string expected_output = "";

        // Create a temporary directory
        std::filesystem::path temp_dir = std::filesystem::temp_directory_path();
        std::string input_file_path = (temp_dir / "input.txt").string();
        std::string output_file_path = (temp_dir / "output.txt").string();

        // Write input text to the temporary input file
        std::ofstream input_file(input_file_path);
        input_file << input_text;
        input_file.close();

        // Call the format_text function
        format_text(input_file_path, output_file_path);

        // Read the output file
        std::ifstream output_file(output_file_path);
        std::string output_text((std::istreambuf_iterator<char>(output_file)), std::istreambuf_iterator<char>());
        output_file.close();

        // Check the output
        REQUIRE(expected_output == output_text);

        // Clean up
        std::remove(input_file_path.c_str());
        std::remove(output_file_path.c_str());
    }

    SECTION("test_file_with_no_newlines") {
        // Test with text that has no newlines
        std::string input_text = "This is a continuous line without breaks.";
        std::string expected_output = "This is a continuous line without breaks.";

        // Create a temporary directory
        std::filesystem::path temp_dir = std::filesystem::temp_directory_path();
        std::string input_file_path = (temp_dir / "input.txt").string();
        std::string output_file_path = (temp_dir / "output.txt").string();

        // Write input text to the temporary input file
        std::ofstream input_file(input_file_path);
        input_file << input_text;
        input_file.close();

        // Call the format_text function
        format_text(input_file_path, output_file_path);

        // Read the output file
        std::ifstream output_file(output_file_path);
        std::string output_text((std::istreambuf_iterator<char>(output_file)), std::istreambuf_iterator<char>());
        output_file.close();

        // Check the output
        REQUIRE(expected_output == output_text);

        // Clean up
        std::remove(input_file_path.c_str());
        std::remove(output_file_path.c_str());
    }
}