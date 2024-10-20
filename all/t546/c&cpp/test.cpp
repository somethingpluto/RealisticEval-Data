TEST_CASE("Test basic TSV input") {
    // Redirect standard input to a stringstream
    std::istringstream input_stream("col1\tcol2\tcol3\nval1\tval2\tval3\n");
    std::streambuf* prev_cin = std::cin.rdbuf(input_stream.rdbuf());

    // Expected output
    const std::vector<std::vector<std::string>> expected_output = {
        {"col1", "col2", "col3"},
        {"val1", "val2", "val3"}
    };

    // Call the function
    const auto result = read_tsv_from_stdin();

    // Restore the original standard input
    std::cin.rdbuf(prev_cin);

    // Check the result
    REQUIRE(result == expected_output);
}

TEST_CASE("Test single column") {
    // Redirect standard input to a stringstream
    std::istringstream input_stream("col1\nval1\nval2\n");
    std::streambuf* prev_cin = std::cin.rdbuf(input_stream.rdbuf());

    // Expected output
    const std::vector<std::vector<std::string>> expected_output = {
        {"col1"},
        {"val1"},
        {"val2"}
    };

    // Call the function
    const auto result = read_tsv_from_stdin();

    // Restore the original standard input
    std::cin.rdbuf(prev_cin);

    // Check the result
    REQUIRE(result == expected_output);
}