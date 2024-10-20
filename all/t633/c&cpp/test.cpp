TEST_CASE_METHOD(TestAnswer, "test_read_valid_csv") {
    auto result = read_csv(test_file_path);
    REQUIRE(result.size() == 4); // 4 lines including the header
    REQUIRE(result[0] == std::vector<std::string>{"Name", "Age", "Location"}); // Check header
    REQUIRE(result[1] == std::vector<std::string>{"Alice", "30", "New York"});
    REQUIRE(result[2] == std::vector<std::string>{"Bob", "25", "Los Angeles"});
    REQUIRE(result[3] == std::vector<std::string>{"Charlie", "35", "Chicago"});
}

TEST_CASE_METHOD(TestAnswer, "test_read_empty_csv") {
    // Create an empty CSV file
    std::ofstream file(test_file_path);
    file << "";
    file.close();
    auto result = read_csv(test_file_path);
    REQUIRE(result.empty()); // Expecting an empty list
}

TEST_CASE_METHOD(TestAnswer, "test_read_csv_with_quotes") {
    // Write CSV content with quoted fields
    std::string content_with_quotes = "\"Name\",\"Age\",\"Location\"\n"
                                       "\"Alice\",\"30\",\"New York\"\n"
                                       "\"Bob\",\"25\",\"Los Angeles\"\n";
    std::ofstream file(test_file_path);
    file << content_with_quotes;
    file.close();
    auto result = read_csv(test_file_path);
    REQUIRE(result.size() == 3); // 3 lines including the header
    REQUIRE(result[0] == std::vector<std::string>{"Name", "Age", "Location"});
}

TEST_CASE("test_read_invalid_csv_file") {
    REQUIRE_THROWS_AS(read_csv("non_existent_file.csv"), std::ifstream::failure);
}

TEST_CASE_METHOD(TestAnswer, "test_read_csv_with_different_delimiters") {
    // Write CSV content with semicolons instead of commas
    std::string content_with_semicolons = "Name;Age;Location\n"
                                           "Alice;30;New York\n"
                                           "Bob;25;Los Angeles\n";
    std::ofstream file(test_file_path);
    file << content_with_semicolons;
    file.close();
    auto result = read_csv(test_file_path);
    REQUIRE(result.size() == 3); // Expecting 3 lines
    REQUIRE(result[0] == std::vector<std::string>{"Name;Age;Location"});
}