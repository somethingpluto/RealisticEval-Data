TEST_CASE("read_columns", "[read_columns]") {
    // Create a temporary file with test data
    const std::string temp_file_name = "temp_data.txt";
    std::ofstream temp_file(temp_file_name);
    temp_file << "This is a test\n"
              << "1 2 3\n"
              << "4 5 6\n"
              << "/\n"
              << "7 8 9\n"
              << "10 11 12\n";
    temp_file.close();

    SECTION("File contains divider") {
        auto result = read_columns(temp_file_name);

        REQUIRE(result.size() == 2);
        REQUIRE(result[0].size() == 3);
        REQUIRE(result[1].size() == 3);
        REQUIRE(result[0][0] == 7);
        REQUIRE(result[0][1] == 8);
        REQUIRE(result[0][2] == 9);
        REQUIRE(result[1][0] == 10);
        REQUIRE(result[1][1] == 11);
        REQUIRE(result[1][2] == 12);
    }

    SECTION("File does not contain divider") {
        std::ofstream empty_temp_file("empty_temp_data.txt");
        empty_temp_file.close();
        REQUIRE_THROWS(read_columns("empty_temp_data.txt"));
    }

    // Clean up the temporary files
    remove(temp_file_name.c_str());
    remove("empty_temp_data.txt");
}