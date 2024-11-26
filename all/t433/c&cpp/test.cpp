TEST_CASE("Test extract_paragraphs_and_lines") {
    SECTION("Single paragraph") {
        std::string input_text = "This is a single paragraph.";
        std::map<std::string, std::vector<std::string>> expected_output = {
            {"paragraphs", {"This is a single paragraph."}},
            {"lines", {"This is a single paragraph."}}
        };

        auto result = extract_paragraphs_and_lines(input_text);
        REQUIRE(result["paragraphs"] == expected_output["paragraphs"]);
        REQUIRE(result["lines"] == expected_output["lines"]);
    }


    SECTION("Empty string") {
        std::string input_text = "";
        std::map<std::string, std::vector<std::string>> expected_output = {
            {"paragraphs", {}},
            {"lines", {}}
        };

        auto result = extract_paragraphs_and_lines(input_text);
        REQUIRE(result["paragraphs"] == expected_output["paragraphs"]);
        REQUIRE(result["lines"] == expected_output["lines"]);
    }

    SECTION("Multiple empty paragraphs") {
        std::string input_text = "\n\n\n";
        std::map<std::string, std::vector<std::string>> expected_output = {
            {"paragraphs", {}},
            {"lines", {}}
        };

        auto result = extract_paragraphs_and_lines(input_text);
        REQUIRE(result["paragraphs"] == expected_output["paragraphs"]);
        REQUIRE(result["lines"] == expected_output["lines"]);
    }
}