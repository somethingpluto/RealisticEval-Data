TEST_CASE_METHOD(TestAnswer, "Test write_csv_to_file with multiple strings") {
    std::vector<std::string> data = {"Apple", "Banana", "Cherry"};
    write_csv_to_file(data, test_file_path);
    // Assert the content of the file
    std::string content = read_file(test_file_path);
    REQUIRE(content == "Apple,Banana,Cherry");
}

TEST_CASE_METHOD(TestAnswer, "Test write_csv_to_file with single string") {
    std::vector<std::string> data = {"Apple"};
    write_csv_to_file(data, test_file_path);
    // Assert the content of the file
    std::string content = read_file(test_file_path);
    REQUIRE(content == "Apple");
}

TEST_CASE_METHOD(TestAnswer, "Test write_csv_to_file with empty list") {
    std::vector<std::string> data = {};
    write_csv_to_file(data, test_file_path);
    // Assert the content of the file is empty
    std::string content = read_file(test_file_path);
    REQUIRE(content == "");
}

TEST_CASE_METHOD(TestAnswer, "Test write_csv_to_file with special characters") {
    std::vector<std::string> data = {"Apple", "Banana, Cherry", "Date"};
    write_csv_to_file(data, test_file_path);
    // Assert the content of the file
    std::string content = read_file(test_file_path);
    REQUIRE(content == "Apple,Banana, Cherry,Date");
}

TEST_CASE_METHOD(TestAnswer, "Test write_csv_to_file with spaces") {
    std::vector<std::string> data = {"Apple ", " Banana", " Cherry "};
    write_csv_to_file(data, test_file_path);
    // Assert the content of the file with spaces
    std::string content = read_file(test_file_path);
    REQUIRE(content == "Apple , Banana, Cherry ");
}

TEST_CASE_METHOD(TestAnswer, "Test write_csv_to_file with file overwrite") {
    // First write to the file
    std::vector<std::string> first_data = {"Apple", "Banana"};
    write_csv_to_file(first_data, test_file_path);

    // Now overwrite with new data
    std::vector<std::string> second_data = {"Cherry", "Date"};
    write_csv_to_file(second_data, test_file_path);

    // Assert that the file now contains the new data
    std::string content = read_file(test_file_path);
    REQUIRE(content == "Cherry,Date");
}