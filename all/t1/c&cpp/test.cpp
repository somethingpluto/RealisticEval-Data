TEST_CASE("Test Smart Convert") {
    SECTION("Convert Integer") {
        REQUIRE(numerical_str_convert("123").intValue == 123);
    }

    SECTION("Convert Float") {
        REQUIRE(numerical_str_convert("123.45").floatValue == Approx(123.45f));
    }

    SECTION("Convert Non-Numeric String") {
        REQUIRE(numerical_str_convert("abc").stringValue == "abc");
    }

    SECTION("Convert Negative Integer") {
        REQUIRE(numerical_str_convert("-456").intValue == -456);
    }

    SECTION("Convert Negative Float") {
        REQUIRE(numerical_str_convert("-456.78").floatValue == Approx(-456.78f));
    }
}