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

    SECTION("Multiple paragraphs") {
        std::string input_text = "First paragraph.\nThis is the second line.\n\nSecond paragraph.\nAnother line.";
        std::map<std::string, std::vector<std::string>> expected_output = {
            {"paragraphs", {"First paragraph.\nThis is the second line.", "Second paragraph.\nAnother line."}},
            {"lines", {"First paragraph.", "This is the second line.", "Second paragraph.", "Another line."}}
        };

        auto result = extract_paragraphs_and_lines(input_text);
        REQUIRE(result["paragraphs"] == expected_output["paragraphs"]);
        REQUIRE(result["lines"] == expected_output["lines"]);
    }

    SECTION("Leading and trailing whitespace") {
        std::string input_text = "   This paragraph has leading whitespace.\nAnd a line after.\n\n   This one has trailing whitespace.   ";
        std::map<std::string, std::vector<std::string>> expected_output = {
            {"paragraphs", {"This paragraph has leading whitespace.\nAnd a line after.", "This one has trailing whitespace."}},
            {"lines", {"This paragraph has leading whitespace.", "And a line after.", "This one has trailing whitespace."}}
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