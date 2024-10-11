TEST_CASE("splitComma function tests") {
    std::vector<std::string> result;

    SECTION("Basic comma-separated values") {
        splitComma("apple,banana,orange", result);
        REQUIRE(result.size() == 3);
        REQUIRE(result[0] == "apple");
        REQUIRE(result[1] == "banana");
        REQUIRE(result[2] == "orange");
    }

    SECTION("Leading and trailing whitespace") {
        splitComma("  apple , banana , orange  ", result);
        REQUIRE(result.size() == 3);
        REQUIRE(result[0] == "apple");
        REQUIRE(result[1] == "banana");
        REQUIRE(result[2] == "orange");
    }

    SECTION("Multiple consecutive commas") {
        splitComma("apple,,banana,,,orange", result);
        REQUIRE(result.size() == 3);
        REQUIRE(result[0] == "apple");
        REQUIRE(result[1] == "banana");
        REQUIRE(result[2] == "orange");
    }

    SECTION("Empty input string") {
        splitComma("", result);
        REQUIRE(result.size() == 0);
    }

    SECTION("Only whitespace input") {
        splitComma("   ", result);
        REQUIRE(result.size() == 0);
    }

    SECTION("Trailing commas") {
        splitComma("apple,banana,orange,", result);
        REQUIRE(result.size() == 3);
        REQUIRE(result[0] == "apple");
        REQUIRE(result[1] == "banana");
        REQUIRE(result[2] == "orange");
    }
}