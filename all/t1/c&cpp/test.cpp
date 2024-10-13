TEST_CASE("Test Smart Convert") {
    SECTION("Convert Integer") {
        REQUIRE(numericalStrConvert("123").intValue == 123);
    }

    SECTION("Convert Float") {
        REQUIRE(numericalStrConvert("123.45").floatValue == Approx(123.45f));
    }

    SECTION("Convert Non-Numeric String") {
        REQUIRE(numericalStrConvert("abc").stringValue == "abc");
    }

    SECTION("Convert Negative Integer") {
        REQUIRE(numericalStrConvert("-456").intValue == -456);
    }

    SECTION("Convert Negative Float") {
        REQUIRE(numericalStrConvert("-456.78").floatValue == Approx(-456.78f));
    }
}