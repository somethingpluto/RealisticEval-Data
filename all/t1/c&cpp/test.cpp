TEST_CASE("numericalStrConvert function tests") {
    SECTION("should convert integer") {
        REQUIRE(std::get<int>(numericalStrConvert("123")) == 123);
    }

    SECTION("should convert float") {
        REQUIRE(std::get<double>(numericalStrConvert("123.45")) == Approx(123.45));
    }

    SECTION("should remain a string for non-numeric input") {
        REQUIRE(std::get<std::string>(numericalStrConvert("abc")) == "abc");
    }

    SECTION("should convert negative integer") {
        REQUIRE(std::get<int>(numericalStrConvert("-456")) == -456);
    }

    SECTION("should convert negative float") {
        REQUIRE(std::get<double>(numericalStrConvert("-456.78")) == Approx(-456.78));
    }
}