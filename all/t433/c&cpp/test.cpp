TEST_CASE("Test extract_paragraphs_and_lines") {
    SECTION("Empty text") {
        auto result = extract_paragraphs_and_lines("");
        REQUIRE(result["paragraphs"].empty());
        REQUIRE(result["lines"].empty());
    }

    SECTION("Single paragraph and single line") {
        auto result = extract_paragraphs_and_lines("First paragraph.");
        REQUIRE(result["paragraphs"].size() == 1);
        REQUIRE(result["paragraphs"][0] == "First paragraph.");
        REQUIRE(result["lines"].size() == 1);
        REQUIRE(result["lines"][0] == "First paragraph.");
    }

    SECTION("Multiple paragraphs and multiple lines") {
        auto result = extract_paragraphs_and_lines("First paragraph.\nThis is the second line.\n\nSecond paragraph.\nAnother line.");
        REQUIRE(result["paragraphs"].size() == 2);
        REQUIRE(result["paragraphs"][0] == "First paragraph.\nThis is the second line.");
        REQUIRE(result["paragraphs"][1] == "Second paragraph.\nAnother line.");
        REQUIRE(result["lines"].size() == 4);
        REQUIRE(result["lines"][0] == "First paragraph.");
        REQUIRE(result["lines"][1] == "This is the second line.");
        REQUIRE(result["lines"][2] == "Second paragraph.");
        REQUIRE(result["lines"][3] == "Another line.");
    }

    SECTION("Single empty paragraph") {
        auto result = extract_paragraphs_and_lines("\n");
        REQUIRE(result["paragraphs"].empty());
        REQUIRE(result["lines"].size() == 0);
    }

    SECTION("Multiple empty paragraphs") {
        auto result = extract_paragraphs_and_lines("\n\n\n");
        REQUIRE(result["paragraphs"].empty());
        REQUIRE(result["lines"].empty());
    }
}