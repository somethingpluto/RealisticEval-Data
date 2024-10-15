namespace fs {
    std::vector<std::string> readdirSync(const std::string& dir) {
        // Placeholder for mocking
        return {};
    }

    bool isDirectory(const std::string& path) {
        // Placeholder for mocking
        return false;
    }

    void mockReaddirSync(const std::vector<std::string>& files) {
        readdirSync = [files](const std::string&) { return files; };
    }

    void mockStatSync(const std::function<bool(const std::string&)>& statFunc) {
        isDirectory = [statFunc](const std::string& path) { return statFunc(path); };
    }
}


TEST_CASE("findMarkdownFiles tests", "[findMarkdownFiles]") {
    // Test for an empty directory
    SECTION("should return an empty array for an empty directory") {
        fs::mockReaddirSync({});
        fs::mockStatSync([](const std::string&) { return false; });

        auto result = findMarkdownFiles("emptyDir");
        REQUIRE(result == std::vector<std::string>{});
    }

    // Test for one Markdown file
    SECTION("should return an array with one Markdown file") {
        fs::mockReaddirSync({"file1.md"});
        fs::mockStatSync([](const std::string&) { return false; });

        auto result = findMarkdownFiles("dir");
        REQUIRE(result == std::vector<std::string>{"file1.md"});
    }

    // Test for multiple Markdown files in the same directory
    SECTION("should return an array with multiple Markdown files in the same directory") {
        fs::mockReaddirSync({"file1.md", "file2.md"});
        fs::mockStatSync([](const std::string&) { return false; });

        auto result = findMarkdownFiles("dir");
        REQUIRE(result == std::vector<std::string>{"file1.md", "file2.md"});
    }

    // Test for ignoring non-Markdown files
    SECTION("should return Markdown files while ignoring non-Markdown files") {
        fs::mockReaddirSync({"file1.txt", "file2.md", "file3.doc"});
        fs::mockStatSync([](const std::string&) { return false; });

        auto result = findMarkdownFiles("dir");
        REQUIRE(result == std::vector<std::string>{"file2.md"});
    }

    // Test for a directory with only non-Markdown files
    SECTION("should handle a directory with only non-Markdown files") {
        fs::mockReaddirSync({"file1.txt", "file2.doc"});
        fs::mockStatSync([](const std::string&) { return false; });

        auto result = findMarkdownFiles("dir");
        REQUIRE(result == std::vector<std::string>{});
    }
}