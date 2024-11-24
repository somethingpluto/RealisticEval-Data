TEST_CASE("Test is_phrase_in_string_ignore_case", "[is_phrase_in_string_ignore_case]") {
    SECTION("Partial word match case insensitive") {
        REQUIRE(is_phrase_in_string_ignore_case("Hello", "saying Hello there"));
    }

    SECTION("Different cases") {
        REQUIRE(is_phrase_in_string_ignore_case("HELLO", "hello there!"));
        REQUIRE(is_phrase_in_string_ignore_case("world", "WORLD is great"));
    }

    SECTION("Non-existent phrase") {
        REQUIRE_FALSE(is_phrase_in_string_ignore_case("goodbye", "Hello world"));
        REQUIRE_FALSE(is_phrase_in_string_ignore_case("hello", "goodbye world"));
    }
}