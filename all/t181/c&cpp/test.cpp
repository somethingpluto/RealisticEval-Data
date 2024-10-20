TEST_CASE("Test reading an empty file") {
    std::string empty_file = "emptyFile.txt";
    std::ofstream(empty_file); // Create an empty file

    auto content = read_file_to_byte_array(empty_file);
    REQUIRE(content.size() == 0);

    std::filesystem::remove(empty_file); // Cleanup
}

TEST_CASE("Test reading a file that does not exist") {
    std::string non_existent_file_path = "nonExistentFile.txt";
    REQUIRE_THROWS_AS(read_file_to_byte_array(non_existent_file_path), std::runtime_error);
}

TEST_CASE("Test reading a file with special characters in its content") {
    std::string special_content = "Special content: !@#$%^&*()_+";
    std::string test_file = "testFile.txt";

    std::ofstream f(test_file, std::ios::binary);
    f.write(special_content.c_str(), special_content.size());

    auto content = read_file_to_byte_array(test_file);
    REQUIRE(content == std::vector<char>(special_content.begin(), special_content.end()));
}

TEST_CASE("Test reading a large file") {
    std::string test_file = "testFile.txt";
    std::vector<char> large_content(256);
    for (int i = 0; i < 256; ++i) {
        large_content[i] = static_cast<char>(i);
    }
    large_content.resize(10 * 1024 * 256); // 10 MB

    std::ofstream f(test_file, std::ios::binary);
    f.write(large_content.data(), large_content.size());

    auto content = read_file_to_byte_array(test_file);
    REQUIRE(content == large_content);