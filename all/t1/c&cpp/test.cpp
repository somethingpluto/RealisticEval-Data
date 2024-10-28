TEST_CASE("SmartConvert Tests", "[numericalStrConvert]") {
    SECTION("Convert integer") {
        REQUIRE(numerical_str_convert("123") == 123);
    }

    SECTION("Convert float") {
        REQUIRE(numerical_str_convert("123.45") == 123.45f);
    }

    SECTION("Convert non-numeric string") {
        REQUIRE(numerical_str_convert("abc") == "abc");
    }

    SECTION("Convert negative integer") {
        REQUIRE(numerical_str_convert("-456") == -456);
    }

    SECTION("Convert negative float") {
        REQUIRE(numerical_str_convert("-456.78") == -456.78f);
    }
}