#define CATCH_CONFIG_MAIN
#include <catch2/catch.hpp>
#include "your_header_file.h" // Replace with the actual header file containing the function

TEST_CASE("parseMarkdownTitles") {
    SECTION("should extract first, second, and third level titles") {
        std::string markdown = R"(
        # Title 1
        Content here.

        ## Subtitle 1.1
        More content.

        ### Subsubtitle 1.1.1
        Even more content.

        # Title 2
        Another content.
        )";

        auto result = parseMarkdownTitles(markdown);
        REQUIRE(result["level1"] == std::vector<std::string>{"Title 1", "Title 2"});
        REQUIRE(result["level2"] == std::vector<std::string>{"Subtitle 1.1"});
        REQUIRE(result["level3"] == std::vector<std::string>{"Subsubtitle 1.1.1"});
    }

    SECTION("should handle missing headers") {
        std::string markdown = R"(
        This is just some text without headers.
        )";

        auto result = parseMarkdownTitles(markdown);
        REQUIRE(result["level1"].empty());
        REQUIRE(result["level2"].empty());
        REQUIRE(result["level3"].empty());
    }

    SECTION("should handle only first-level headers") {
        std::string markdown = R"(
        # Only Title 1
        Content without subtitles.

        # Only Title 2
        More content.
        )";

        auto result = parseMarkdownTitles(markdown);
        REQUIRE(result["level1"] == std::vector<std::string>{"Only Title 1", "Only Title 2"});
        REQUIRE(result["level2"].empty());
        REQUIRE(result["level3"].empty());
    }

    SECTION("should handle mixed headers with empty lines") {
        std::string markdown = R"(
        # Title 1

        ## Subtitle 1.1

        Some content here.

        ### Subsubtitle 1.1.1

        # Title 2
        )";

        auto result = parseMarkdownTitles(markdown);
        REQUIRE(result["level1"] == std::vector<std::string>{"Title 1", "Title 2"});
        REQUIRE(result["level2"] == std::vector<std::string>{"Subtitle 1.1"});
        REQUIRE(result["level3"] == std::vector<std::string>{"Subsubtitle 1.1.1"});
    }

    SECTION("should handle headers with special characters") {
        std::string markdown = R"(
        # Title 1 - Special Characters!
        ## Subtitle 1.1: The Beginning
        ### Subsubtitle 1.1.1 (Note)
        )";

        auto result = parseMarkdownTitles(markdown);
        REQUIRE(result["level1"] == std::vector<std::string>{"Title 1 - Special Characters!"});
        REQUIRE(result["level2"] == std::vector<std::string>{"Subtitle 1.1: The Beginning"});
        REQUIRE(result["level3"] == std::vector<std::string>{"Subsubtitle 1.1.1 (Note)"});
    }
}