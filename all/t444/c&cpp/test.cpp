#define CATCH_CONFIG_MAIN
#include <catch2/catch.hpp>
#include "your_source_file.h" // Include the header where format_comment is defined

TEST_CASE("Format Comment", "[format_comment]") {
    SECTION("Empty String") {
        REQUIRE(format_comment("") == "");
    }

    SECTION("Single Word") {
        REQUIRE(format_comment("Hello") == "# Hello");
    }

    SECTION("Long Single Line") {
        std::string long_string = "ThisIsAVeryLongStringThatShouldBeSplitIntoMultipleLines";
        std::string expected = "# ThisIsAVeryLongStringThat\n# ShouldBeSplitIntoMultipleLines";
        REQUIRE(format_comment(long_string) == expected);
    }

    SECTION("Words That Fit In One Line") {
        REQUIRE(format_comment("One Two Three Four Five") == "# One Two Three Four Five");
    }

    SECTION("Words Exceeding Max Length") {
        std::string long_words = "Lorem ipsum dolor sit amet, consectetur adipiscing elit.";
        std::string expected = "# Lorem ipsum dolor sit amet,\n# consectetur adipiscing elit.";
        REQUIRE(format_comment(long_words) == expected);
    }
}