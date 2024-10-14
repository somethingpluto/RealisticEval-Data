TEST_CASE("Compressing whitespace", "[compress_whitespace]") {
    SECTION("Single space") {
        REQUIRE(compress_whitespace("hello world") == "hello world");
    }

    SECTION("Multiple consecutive spaces") {
        REQUIRE(compress_whitespace("hello   world") == "hello world");
    }

    SECTION("Leading and trailing spaces") {
        REQUIRE(compress_whitespace("  hello  world  ") == "hello world");
    }

    SECTION("All spaces") {
        REQUIRE(compress_whitespace("      ") == " ");
    }

    SECTION("No spaces") {
        REQUIRE(compress_whitespace("helloworld") == "helloworld");
    }

    SECTION("Mixed content") {
        REQUIRE(compress_whitespace("hello  world  again") == "hello world again");
    }
}