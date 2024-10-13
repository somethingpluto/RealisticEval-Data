TEST_CASE("Test Compare Files") {
    // Create temporary files for testing
    const std::string file1_path = "file1.txt";
    const std::string file2_path = "file2.txt";

    SECTION("Identical Files") {
        std::string file1_content = "Line1\nLine2\nLine3\n";
        std::string file2_content = "Line1\nLine2\nLine3\n";

        std::ofstream f1(file1_path);
        std::ofstream f2(file2_path);
        f1 << file1_content;
        f2 << file2_content;

        REQUIRE(compare_files(file1_path, file2_path).empty());
    }

    SECTION("Files with Differences") {
        std::string file1_content = "Line1\nLine2\nLine3\n";
        std::string file2_content = "Line1\nLineChanged\nLine3\n";

        std::ofstream f1(file1_path);
        std::ofstream f2(file2_path);
        f1 << file1_content;
        f2 << file2_content;

        auto result = compare_files(file1_path, file2_path);
        REQUIRE(!result.empty());
    }

    SECTION("Nonexistent File") {
        REQUIRE_THROWS_AS(compare_files("nonexistent.txt", file2_path), std::runtime_error);
    }

    SECTION("File Reading Error") {
        // Simulate file reading error by creating a file that cannot be read
        std::ofstream f1(file1_path);
        f1 << "Line1\nLine2\nLine3\n";

        // Change file permissions to make it unreadable
        fs::permissions(file1_path, fs::perms::none);

        REQUIRE_THROWS_AS(compare_files(file1_path, file2_path), std::runtime_error);

        // Restore file permissions
        fs::permissions(file1_path, fs::perms::owner_read | fs::perms::owner_write);
    }

    // Clean up temporary files
    if (fs::exists(file1_path)) {
        fs::remove(file1_path);
    }
    if (fs::exists(file2_path)) {
        fs::remove(file2_path);
    }
}