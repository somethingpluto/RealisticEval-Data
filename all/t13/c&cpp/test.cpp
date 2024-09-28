#define CATCH_CONFIG_MAIN  // This tells Catch to provide a main() - only do this in one cpp file
#include <catch2/catch.hpp>
#include <vector>
#include <string>
#include <tuple>
#include <algorithm>
#include <sstream>

// Declare the parse_markdown_table function here (same as the previously provided C++ implementation)
std::vector<std::vector<std::string>> parse_markdown_table(const std::string &md_table);

// Helper function to compare vectors of vectors
bool compareTable(const std::vector<std::vector<std::string>>& result, const std::vector<std::vector<std::string>>& expected) {
    if (result.size() != expected.size()) return false;
    for (size_t i = 0; i < result.size(); ++i) {
        if (result[i].size() != expected[i].size()) return false;
        for (size_t j = 0; j < result[i].size(); ++j) {
            if (result[i][j] != expected[i][j]) return false;
        }
    }
    return true;
}

TEST_CASE("Standard table") {
    std::string md_table = R"(
        | Header 1 | Header 2 | Header 3 |
        |----------|----------|----------|
        | Row1Col1 | Row1Col2 | Row1Col3 |
        | Row2Col1 | Row2Col2 | Row2Col3 |
    )";

    std::vector<std::vector<std::string>> expected = {
        {"Header 1", "Header 2", "Header 3"},
        {"Row1Col1", "Row1Col2", "Row1Col3"},
        {"Row2Col1", "Row2Col2", "Row2Col3"}
    };

    auto result = parse_markdown_table(md_table);
    REQUIRE(compareTable(result, expected));
}

TEST_CASE("Inconsistent columns") {
    std::string md_table = R"(
        | Header 1 | Header 2 |
        |----------|----------|
        | Row1     | Row1Col2 | ExtraCol |
        | Row2     |
    )";

    std::vector<std::vector<std::string>> expected = {
        {"Header 1", "Header 2"},
        {"Row1", "Row1Col2", "ExtraCol"},
        {"Row2"}
    };

    auto result = parse_markdown_table(md_table);
    REQUIRE(compareTable(result, expected));
}

TEST_CASE("Empty cells") {
    std::string md_table = R"(
        | Header 1 | Header 2 | Header 3 |
        |----------|----------|----------|
        |          | Row1Col2 |          |
        | Row2Col1 |          | Row2Col3 |
    )";

    std::vector<std::vector<std::string>> expected = {
        {"Header 1", "Header 2", "Header 3"},
        {"", "Row1Col2", ""},
        {"Row2Col1", "", "Row2Col3"}
    };

    auto result = parse_markdown_table(md_table);
    REQUIRE(compareTable(result, expected));
}

TEST_CASE("All empty rows") {
    std::string md_table = R"(
        | Header 1 | Header 2 | Header 3 |
        |----------|----------|----------|
        |          |          |          |
        |          |          |          |
    )";

    std::vector<std::vector<std::string>> expected = {
        {"Header 1", "Header 2", "Header 3"},
        {"", "", ""},
        {"", "", ""}
    };

    auto result = parse_markdown_table(md_table);
    REQUIRE(compareTable(result, expected));
}

TEST_CASE("Excessive whitespace") {
    std::string md_table = R"(
        |  Header 1  |  Header 2  |  Header 3  |
        |------------|------------|------------|
        |  Row1Col1  |  Row1Col2  |  Row1Col3  |
        |  Row2Col1  |  Row2Col2  |  Row2Col3  |
    )";

    std::vector<std::vector<std::string>> expected = {
        {"Header 1", "Header 2", "Header 3"},
        {"Row1Col1", "Row1Col2", "Row1Col3"},
        {"Row2Col1", "Row2Col2", "Row2Col3"}
    };

    auto result = parse_markdown_table(md_table);
    REQUIRE(compareTable(result, expected));
}

// Simple implementation of parse_markdown_table for demonstration (fill with actual code)
std::vector<std::vector<std::string>> parse_markdown_table(const std::string &md_table) {
    // This is a placeholder. Use the provided C++ implementation from the earlier sections.
    return {};
}