TEST_CASE("Test read_csv_to_data_structure", "[read_csv]") {
    const std::string file_path = "path/to/your/file.csv";
    std::vector<std::vector<std::string>> data = read_csv_to_data_structure(file_path);

    SECTION("File exists and is not empty") {
        REQUIRE(!data.empty());
        REQUIRE(data.size() > 1); // Ensure there are headers and at least one row

        // Example check for headers
        REQUIRE(data[0].size() == 3); // Assuming 3 headers
        REQUIRE(data[0][0] == "header1");
        REQUIRE(data[0][1] == "header2");
        REQUIRE(data[0][2] == "header3");

        // Example check for rows
        REQUIRE(data[1].size() == 3); // Assuming 3 columns
        REQUIRE(data[1][0] == "value1");
        REQUIRE(data[1][1] == "value2");
        REQUIRE(data[1][2] == "value3");
    }

    SECTION("File does not exist") {
        const std::string non_existent_file_path = "path/to/nonexistent/file.csv";
        std::vector<std::vector<std::string>> non_existent_data = read_csv_to_data_structure(non_existent_file_path);
        REQUIRE(non_existent_data.empty());
    }

    SECTION("File is empty") {
        const std::string empty_file_path = "path/to/empty/file.csv";
        std::vector<std::vector<std::string>> empty_data = read_csv_to_data_structure(empty_file_path);
        REQUIRE(empty_data.empty());
    }
}