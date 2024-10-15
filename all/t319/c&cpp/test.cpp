TEST_CASE("countDashes") {
    SECTION("should return 0 for a string with no dashes") {
        REQUIRE(countDashes("hello world") == 0); // 'hello world' contains no dashes
    }

    SECTION("should return 1 for a string with one dash") {
        REQUIRE(countDashes("hello-world") == 1); // 'hello-world' contains one dash
    }

    SECTION("should return 4 for a string with multiple dashes") {
        REQUIRE(countDashes("a-b-c-d-e") == 4); // 'a-b-c-d-e' contains four dashes
    }

    SECTION("should return 3 for a string with dashes at the beginning and end") {
        REQUIRE(countDashes("-start-end-") == 3); // '-start-end-' contains three dashes
    }

    SECTION("should return 0 for an empty string") {
        REQUIRE(countDashes("") == 0); // An empty string contains no dashes
    }
}