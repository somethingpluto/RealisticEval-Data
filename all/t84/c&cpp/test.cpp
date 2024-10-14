TEST_CASE("Test find_min_window_substring") {
    SECTION("Empty source string") {
        REQUIRE(find_min_window_substring("", "abc") == "");
        // Should return an empty string when source is empty
    }

    SECTION("Empty target string") {
        REQUIRE(find_min_window_substring("abc", "") == "");
        // Should return an empty string when target is empty
    }

    SECTION("No valid window") {
        REQUIRE(find_min_window_substring("abcdef", "xyz") == "");
        // Should return an empty string when no valid window exists
    }

    SECTION("Exact match window") {
        REQUIRE(find_min_window_substring("abcd", "abcd") == "abcd");
        // Should return the entire string when it is an exact match
    }

    SECTION("Minimal valid window") {
        REQUIRE(find_min_window_substring("ADOBECODEBANC", "ABC") == "BANC");
        // Should return 'BANC' as the smallest window containing all characters of 'ABC'
    }
}