#define CATCH_CONFIG_MAIN
#include <catch2/catch.hpp>
#include <string>

// Function prototype (assuming it's defined elsewhere)
std::string convertHtmlHeadingsToMarkdown(const std::string& html);

TEST_CASE("convertHtmlHeadingsToMarkdown") {
    SECTION("should convert <h1> to #") {
        std::string input = "<h1>This is a Heading 1</h1>";
        std::string output = "# This is a Heading 1";
        REQUIRE(convertHtmlHeadingsToMarkdown(input) == output);
    }

    SECTION("should convert <h2> to ##") {
        std::string input = "<h2>This is a Heading 2</h2>";
        std::string output = "## This is a Heading 2";
        REQUIRE(convertHtmlHeadingsToMarkdown(input) == output);
    }

    SECTION("should convert <h3> to ###") {
        std::string input = "<h3>This is a Heading 3</h3>";
        std::string output = "### This is a Heading 3";
        REQUIRE(convertHtmlHeadingsToMarkdown(input) == output);
    }

    SECTION("should convert <h4> to ####") {
        std::string input = "<h4>This is a Heading 4</h4>";
        std::string output = "#### This is a Heading 4";
        REQUIRE(convertHtmlHeadingsToMarkdown(input) == output);
    }

    SECTION("should convert <h5> to #####") {
        std::string input = "<h5>This is a Heading 5</h5>";
        std::string output = "##### This is a Heading 5";
        REQUIRE(convertHtmlHeadingsToMarkdown(input) == output);
    }

    SECTION("should convert <h6> to ######") {
        std::string input = "<h6>This is a Heading 6</h6>";
        std::string output = "###### This is a Heading 6";
        REQUIRE(convertHtmlHeadingsToMarkdown(input) == output);
    }
}