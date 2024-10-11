TEST_CASE("Prepend to Each Line", "[prepend_to_each_line]") {
    std::string test_file = "test.txt";
    std::string expected_output = "prefixLine1\nprefixLine2\n";

    // Create a temporary test file with some content
    std::ofstream temp_file(test_file);
    temp_file << "Line1\nLine2\n";
    temp_file.close();

    try {
        prepend_to_each_line(test_file, "prefix");

        // Read the modified content back from the file
        std::ifstream result_file(test_file);
        std::string actual_output((std::istreambuf_iterator<char>(result_file)), std::istreambuf_iterator<char>());
        result_file.close();

        REQUIRE(actual_output == expected_output);
    } catch (const std::exception& e) {
        REQUIRE(false);  // If an exception was thrown, the test failed
    }

    // Clean up the temporary test file
    std::remove(test_file.c_str());
}