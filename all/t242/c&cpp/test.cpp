TEST_CASE("Test classifyFilesByExtension") {
    SECTION("Test with multiple file types") {
        std::vector<std::string> files = {
            "document.docx",
            "photo.jpeg",
            "report.pdf",
            "image.png",
            "archive.zip"
        };
        std::unordered_map<std::string, std::vector<std::string>> expected_result = {
            {"docx", {"document.docx"}},
            {"jpeg", {"photo.jpeg"}},
            {"pdf", {"report.pdf"}},
            {"png", {"image.png"}},
            {"zip", {"archive.zip"}}
        };

        REQUIRE(classifyFilesByExtension(files) == expected_result);
    }

    SECTION("Test with an empty list of file names") {
        std::vector<std::string> files = {};
        std::unordered_map<std::string, std::vector<std::string>> expected_result = {};

        REQUIRE(classifyFilesByExtension(files) == expected_result);
    }

    SECTION("Test with multiple files having the same extension") {
        std::vector<std::string> files = {
            "file1.txt",
            "file2.txt",
            "file3.txt"
        };
        std::unordered_map<std::string, std::vector<std::string>> expected_result = {
            {"txt", {"file1.txt", "file2.txt", "file3.txt"}}
        };

        REQUIRE(classifyFilesByExtension(files) == expected_result);
    }

    SECTION("Test files that have multiple dots in their names") {
        std::vector<std::string> files = {
            "my.document.docx",
            "report.final.pdf",
            "photo.album.jpeg",
            "archive.backup.zip"
        };
        std::unordered_map<std::string, std::vector<std::string>> expected_result = {
            {"docx", {"my.document.docx"}},
            {"pdf", {"report.final.pdf"}},
            {"jpeg", {"photo.album.jpeg"}},
            {"zip", {"archive.backup.zip"}}
        };

        REQUIRE(classifyFilesByExtension(files) == expected_result);
    }
}