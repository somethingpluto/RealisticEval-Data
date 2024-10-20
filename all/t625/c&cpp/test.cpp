void create_test_file(const std::string& file_name, const std::string& content) {
    std::ofstream writer(file_name);
    writer << content;
    writer.close();
}

TEST_CASE("Read valid integers") {
    std::string file_path = "valid_integers.txt";
    create_test_file(file_path, "42\n-7\n0\n100\n");
    auto result = read_data_from_file(file_path);
    
    REQUIRE(result.size() == 4);
    REQUIRE(std::get<int>(result[0]) == 42);
    REQUIRE(std::get<int>(result[1]) == -7);
    REQUIRE(std::get<int>(result[2]) == 0);
    REQUIRE(std::get<int>(result[3]) == 100);

    std::remove(file_path.c_str()); // Clean up the test file
}

TEST_CASE("Read valid floats") {
    std::string file_path = "valid_floats.txt";
    create_test_file(file_path, "3.14\n-0.001\n2.71828\n0.0\n");
    auto result = read_data_from_file(file_path);
    
    REQUIRE(result.size() == 4);
    REQUIRE(std::get<float>(result[0]) == Approx(3.14f));
    REQUIRE(std::get<float>(result[1]) == Approx(-0.001f));
    REQUIRE(std::get<float>(result[2]) == Approx(2.71828f));
    REQUIRE(std::get<float>(result[3]) == Approx(0.0f));

    std::remove(file_path.c_str()); // Clean up the test file
}

TEST_CASE("Read mixed data") {
    std::string file_path = "mixed_data.txt";
    create_test_file(file_path, "Hello\n42\n3.14\nWorld\n-19.99\n");
    auto result = read_data_from_file(file_path);
    
    REQUIRE(result.size() == 5);
    REQUIRE(std::get<std::string>(result[0]) == "Hello");
    REQUIRE(std::get<int>(result[1]) == 42);
    REQUIRE(std::get<float>(result[2]) == Approx(3.14f));
    REQUIRE(std::get<std::string>(result[3]) == "World");
    REQUIRE(std::get<float>(result[4]) == Approx(-19.99f));

    std::remove(file_path.c_str()); // Clean up the test file
}

TEST_CASE("Read empty file") {
    std::string file_path = "empty_file.txt";
    create_test_file(file_path, "");
    auto result = read_data_from_file(file_path);
    
    REQUIRE(result.size() == 0);

    std::remove(file_path.c_str()); // Clean up the test file
}

TEST_CASE("Read invalid data") {
    std::string file_path = "invalid_data.txt";
    create_test_file(file_path, "Hello\n42a\n3.14.15\nWorld!\n");
    auto result = read_data_from_file(file_path);
    
    REQUIRE(result.size() == 4);
    REQUIRE(std::get<std::string>(result[0]) == "Hello");
    REQUIRE(std::get<std::string>(result[1]) == "42a");
    REQUIRE(std::get<std::string>(result[2]) == "3.14.15");
    REQUIRE(std::get<std::string>(result[3]) == "World!");

    std::remove(file_path.c_str()); // Clean up the test file
}