TEST_CASE("Replace words in file", "[file_replacement]") {
    // Define a sample input file content
    std::string file_content = "hello world\nthis is a test";

    // Write the sample input file to disk
    std::ofstream file("test_input.txt");
    file << file_content;
    file.close();

    // Define the replacement dictionary
    std::unordered_map<std::string, std::string> replacement_dict = {
        {"hello", "hi"},
        {"world", "earth"}
    };

    // Call the function under test
    std::string result = replace_words_in_file("test_input.txt", replacement_dict);

    // Expected output after replacements
    std::string expected_output = "hi earth\ntest is a test";

    // Check if the result matches the expected output
    REQUIRE(result == expected_output);

    // Clean up the temporary file
    remove("test_input.txt");
}