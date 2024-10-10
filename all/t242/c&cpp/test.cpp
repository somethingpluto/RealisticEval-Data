TEST_CASE("Classify files by extension", "[classify_files]") {
    SECTION("Empty list") {
        std::vector<std::string> empty_list = {};
        auto result = classify_files_by_extension(empty_list);
        REQUIRE(result.empty());
    }

    SECTION("List with one file") {
        std::vector<std::string> single_file = {"example.txt"};
        auto result = classify_files_by_extension(single_file);
        REQUIRE(result.size() == 1);
        REQUIRE(result["txt"] == std::vector<std::string>{"example.txt"});
    }

    SECTION("List with multiple files") {
        std::vector<std::string> multiple_files = {"image.png", "document.pdf", "script.py", "data.csv"};
        auto result = classify_files_by_extension(multiple_files);
        REQUIRE(result.size() == 4);
        REQUIRE(result["png"] == std::vector<std::string>{"image.png"});
        REQUIRE(result["pdf"] == std::vector<std::string>{"document.pdf"});
        REQUIRE(result["py"] == std::vector<std::string>{"script.py"});
        REQUIRE(result["csv"] == std::vector<std::string>{"data.csv"});
    }
}