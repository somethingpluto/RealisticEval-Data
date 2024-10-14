TEST_CASE("replaceHtmlEntities") {
    SECTION("decodes standard HTML entities") {
        std::string input = "The &amp; symbol should become an &quot;and&quot; sign.";
        std::string expected = "The & symbol should become an \"and\" sign.";
        REQUIRE(replaceHtmlEntities(input) == expected);
    }

    SECTION("returns empty string for empty input") {
        std::string input = "";
        std::string expected = "";
        REQUIRE(replaceHtmlEntities(input) == expected);
    }

    SECTION("decodes multiple different entities in one string") {
        std::string input = "&lt;div&gt;Hello &amp; Welcome to the &apos;World&apos;!&lt;/div&gt;";
        std::string expected = "<div>Hello & Welcome to the 'World'!</div>";
        REQUIRE(replaceHtmlEntities(input) == expected);
    }

    SECTION("handles strings with no entities") {
        std::string input = "Just a normal string without entities.";
        std::string expected = "Just a normal string without entities.";
        REQUIRE(replaceHtmlEntities(input) == expected);
    }
}