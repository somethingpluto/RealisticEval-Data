TEST_CASE("Empty Directory", "[empty_directory]") {
    // Test cases go here

    SECTION("Non-existent directory") {
        REQUIRE_THROWS_AS(empty_directory("/path/to/nonexistent/directory"), std::invalid_argument);
    }

    SECTION("Non-directory path") {
        REQUIRE_THROWS_AS(empty_directory("/path/to/file.txt"), std::invalid_argument);
    }

    SECTION("Empty directory") {
        fs::create_directories("/tmp/test_dir");
        empty_directory("/tmp/test_dir");
        REQUIRE(fs::directory_iterator("/tmp/test_dir").begin() == fs::directory_iterator("/tmp/test_dir").end());
        fs::remove_all("/tmp/test_dir");
    }

    SECTION("Directory with files") {
        fs::create_directories("/tmp/test_dir");
        fs::create_file("/tmp/test_dir/file1.txt");
        fs::create_file("/tmp/test_dir/file2.txt");
        empty_directory("/tmp/test_dir");
        REQUIRE(fs::directory_iterator("/tmp/test_dir").begin() == fs::directory_iterator("/tmp/test_dir").end());
        fs::remove_all("/tmp/test_dir");
    }
}