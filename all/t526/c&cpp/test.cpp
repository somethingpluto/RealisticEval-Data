// Test class using Catch2
TEST_CASE("Test cases for min_window", "[min_window]") {
    SECTION("Test with a normal case where the minimum window exists") {
        std::string s = "ADOBECODEBANC";
        std::string t = "ABC";
        std::string expected_output = "BANC";
        REQUIRE(min_window(s, t) == expected_output);
    }

    SECTION("Test where no window can satisfy the condition") {
        std::string s = "A";
        std::string t = "AA";
        std::string expected_output = "";
        REQUIRE(min_window(s, t) == expected_output);
    }

    SECTION("Test with an empty input string s") {
        std::string s = "";
        std::string t = "ABC";
        std::string expected_output = "";
        REQUIRE(min_window(s, t) == expected_output);
    }

    SECTION("Test with multiple valid windows to ensure the smallest one is returned") {
        std::string s = "AA";
        std::string t = "AA";
        std::string expected_output = "AA";
        REQUIRE(min_window(s, t) == expected_output);
    }
}