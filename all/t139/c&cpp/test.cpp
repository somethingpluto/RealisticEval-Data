TEST_CASE("parseCategoriesFromSummary") {
    SECTION("extracts categories and cleans the summary correctly") {
        std::string input = "This is a summary. Categories: [Technology, Health]";
        SummaryResult expected = {"This is a summary.", {"Technology", "Health"}};
        REQUIRE(parseCategoriesFromSummary(input) == expected);
    }

    SECTION("returns empty categories and original summary when no categories are present") {
        std::string input = "This is a summary without categories.";
        SummaryResult expected = {"This is a summary without categories.", {}};
        REQUIRE(parseCategoriesFromSummary(input) == expected);
    }

    SECTION("ignores case of the category prefix") {
        std::string input = "Summary text. categories: [Education, Science]";
        SummaryResult expected = {"Summary text.", {"Education", "Science"}};
        REQUIRE(parseCategoriesFromSummary(input) == expected);
    }

    SECTION("handles extra spaces and malformed category strings correctly") {
        std::string input = "Details follow. Categories: [ Business ,  , Finance]";
        SummaryResult expected = {"Details follow.", {"Business", "Finance"}};
        REQUIRE(parseCategoriesFromSummary(input) == expected);
    }

    SECTION("removes the category string correctly even if it appears in the middle of the summary") {
        std::string input = "Beginning of summary. Categories: [Art, Design] Continuation of summary.";
        SummaryResult expected = {"Beginning of summary. Continuation of summary.", {"Art", "Design"}};
        REQUIRE(parseCategoriesFromSummary(input) == expected);
    }
}