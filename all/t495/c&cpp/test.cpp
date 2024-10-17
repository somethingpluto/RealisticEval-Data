#include <iostream>
#include <string>
#include <vector>
#include <regex>
#include <set>
#include <sstream>
#include <catch2/catch_test_macros.hpp>

TEST_CASE("TestFilterContentWithContext", "[filter_content_with_context]") {
    SECTION("test_single_keyword_match") {
        std::string content = R"(Line one.
        This line contains a keyword.
        Line three.)";
        std::vector<std::string> keywords = {"keyword"};
        std::string expected_output = R"(Line one.
        This line contains a keyword.
        Line three.)";
        std::string result = filter_content_with_context(content, keywords, 1, 1);
        REQUIRE(result == expected_output);
    }

    SECTION("test_no_keyword_match") {
        std::string content = R"(Line one.
        Line two.
        Line three.)";
        std::vector<std::string> keywords = {"missing"};
        std::string expected_output = "";
        std::string result = filter_content_with_context(content, keywords, 1, 1);
        REQUIRE(result == expected_output);
    }

    SECTION("test_lines_before_and_after") {
        std::string content = R"(Line one.
        This line contains a keyword.
        Line three.
        Line four.
        Line five.)";
        std::vector<std::string> keywords = {"keyword"};
        std::string expected_output = R"(Line one.
        This line contains a keyword.
        Line three.)";
        std::string result = filter_content_with_context(content, keywords, 1, 1);
        REQUIRE(result == expected_output);
    }
}