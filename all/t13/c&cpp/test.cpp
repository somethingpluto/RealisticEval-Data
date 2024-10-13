TEST_CASE("Test parse_markdown_table", "[parse_markdown_table]") {
    SECTION("test_standard_table") {
        std::string md_table = R"(
        | Header 1 | Header 2 | Header 3 |
        |----------|----------|----------|
        | Row1Col1 | Row1Col2 | Row1Col3 |
        | Row2Col1 | Row2Col2 | Row2Col3 |
        )";
        std::vector<std::tuple<std::string, std::string, std::string>> expected = {
            {"Header 1", "Header 2", "Header 3"},
            {"Row1Col1", "Row1Col2", "Row1Col3"},
            {"Row2Col1", "Row2Col2", "Row2Col3"}
        };
        auto result = parse_markdown_table(md_table);
        REQUIRE(result == expected);
    }

    SECTION("test_inconsistent_columns") {
        std::string md_table = R"(
        | Header 1 | Header 2 |
        |----------|----------|
        | Row1     | Row1Col2 | ExtraCol |
        | Row2     |
        )";
        std::vector<std::tuple<std::string, std::string, std::string>> expected = {
            {"Header 1", "Header 2"},
            {"Row1", "Row1Col2", "ExtraCol"},
            {"Row2"}
        };
        auto result = parse_markdown_table(md_table);
        REQUIRE(result == expected);
    }

    SECTION("test_empty_cells") {
        std::string md_table = R"(
        | Header 1 | Header 2 | Header 3 |
        |----------|----------|----------|
        |          | Row1Col2 |          |
        | Row2Col1 |          | Row2Col3 |
        )";
        std::vector<std::tuple<std::string, std::string, std::string>> expected = {
            {"Header 1", "Header 2", "Header 3"},
            {"", "Row1Col2", ""},
            {"Row2Col1", "", "Row2Col3"}
        };
        auto result = parse_markdown_table(md_table);
        REQUIRE(result == expected);
    }

    SECTION("test_all_empty_rows") {
        std::string md_table = R"(
        | Header 1 | Header 2 | Header 3 |
        |----------|----------|----------|
        |          |          |          |
        |          |          |          |
        )";
        std::vector<std::tuple<std::string, std::string, std::string>> expected = {
            {"Header 1", "Header 2", "Header 3"},
            {"", "", ""},
            {"", "", ""}
        };
        auto result = parse_markdown_table(md_table);
        REQUIRE(result == expected);
    }

    SECTION("test_excessive_whitespace") {
        std::string md_table = R"(
        |  Header 1  |  Header 2  |  Header 3  |
        |------------|------------|------------|
        |  Row1Col1  |  Row1Col2  |  Row1Col3  |
        |  Row2Col1  |  Row2Col2  |  Row2Col3  |
        )";
        std::vector<std::tuple<std::string, std::string, std::string>> expected = {
            {"Header 1", "Header 2", "Header 3"},
            {"Row1Col1", "Row1Col2", "Row1Col3"},
            {"Row2Col1", "Row2Col2", "Row2Col3"}
        };
        auto result = parse_markdown_table(md_table);
        REQUIRE(result == expected);
    }
}