TEST_CASE_METHOD(FileTest, "Test copy file with content") {
    long long time_taken = copy_file_with_buffered_stream(source_file, destination_file);
    
    REQUIRE(std::filesystem::exists(destination_file));
    REQUIRE(std::filesystem::file_size(source_file) == std::filesystem::file_size(destination_file));
    REQUIRE(time_taken >= 0);
}

TEST_CASE("Test copy empty file") {
    std::string empty_file = "emptyFile.txt";
    std::ofstream f(empty_file, std::ios::binary);
    
    std::string destination_empty_file = "destinationEmptyFile.txt";
    long long time_taken = copy_file_with_buffered_stream(empty_file, destination_empty_file);

    REQUIRE(std::filesystem::exists(destination_empty_file));
    REQUIRE(std::filesystem::file_size(destination_empty_file) == 0);
    REQUIRE(time_taken >= 0);

    std::filesystem::remove(empty_file);
    std::filesystem::remove(destination_empty_file);
}

TEST_CASE("Test copy non-existent file") {
    std::string non_existent_file_path = "nonExistentFile.txt";
    REQUIRE_THROWS(copy_file_with_buffered_stream(non_existent_file_path, "someDestination.txt"));
}

TEST_CASE_METHOD(FileTest, "Test copy file overwrite") {
    std::ofstream f(destination_file, std::ios::binary);
    f.write("Old content", 12);
    
    long long time_taken = copy_file_with_buffered_stream(source_file, destination_file);

    REQUIRE(std::filesystem::exists(destination_file));
    REQUIRE(std::filesystem::file_size(source_file) == std::filesystem::file_size(destination_file));
    REQUIRE(time_taken > 0);
}

TEST_CASE("Test copy large file") {
    std::string large_file = "largeFile.txt";
    std::ofstream f(large_file, std::ios::binary);
    
    std::vector<char> large_content(10 * 1024 * 1024); // 10 MB
    for (size_t i = 0; i < large_content.size(); ++i) {
        large_content[i] = static_cast<char>(i % 256);
    }
    f.write(large_content.data(), large_content.size());
    
    std::string destination_large_file = "destinationLargeFile.txt";
    long long time_taken = copy_file_with_buffered_stream(large_file, destination_large_file);

    REQUIRE(std::filesystem::exists(destination_large_file));
    REQUIRE(std::filesystem::file_size(large_file) == std::filesystem::file_size(destination_large_file));
    REQUIRE(time_taken > 0);

    std::filesystem::remove(large_file);
    std::filesystem::remove(destination_large_file);
}