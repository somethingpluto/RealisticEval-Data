TEST_CASE("Find common columns", "[common_columns]") {
    SECTION("Directory with multiple CSV files") {
        std::string directory = "path/to/your/directory";  // Replace with the actual directory path
        std::vector<std::string> expected = {"column1", "column2"};  // Replace with the expected result

        std::vector<std::string> result = find_common_columns(directory);

        REQUIRE(result == expected);
    }

    SECTION("Directory with no CSV files") {
        std::string directory = "path/to/empty/directory";  // Replace with the actual empty directory path
        std::vector<std::string> expected = {};  // Expected result when there are no CSV files

        std::vector<std::string> result = find_common_columns(directory);

        REQUIRE(result == expected);
    }

    SECTION("Directory with single CSV file") {
        std::string directory = "path/to/single_csv_file_directory";  // Replace with the actual directory path
        std::vector<std::string> expected = {"column1", "column2"};  // Replace with the expected result

        std::vector<std::string> result = find_common_columns(directory);

        REQUIRE(result == expected);
    }
}