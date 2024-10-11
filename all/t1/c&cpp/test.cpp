TEST_CASE("numerical_str_convert") {
    SECTION("Convert valid integer strings") {
        REQUIRE(std::get<int>(numerical_str_convert("42")) == 42);
        REQUIRE(std::get<int>(numerical_str_convert("-42")) == -42);
    }

    SECTION("Convert valid float strings") {
        REQUIRE(std::get<float>(numerical_str_convert("3.14")) == Approx(3.14f));
        REQUIRE(std::get<float>(numerical_str_convert("-3.14")) == Approx(-3.14f));
        REQUIRE(std::get<float>(numerical_str_convert("0.001")) == Approx(0.001f));
    }

    SECTION("Return original string for invalid inputs") {
        REQUIRE(std::get<std::string>(numerical_str_convert("abc")) == "abc");
        REQUIRE(std::get<std::string>(numerical_str_convert("3.14abc")) == "3.14abc");
    }

    SECTION("Return original string for empty input") {
        REQUIRE(std::get<std::string>(numerical_str_convert("")) == "");
    }
}