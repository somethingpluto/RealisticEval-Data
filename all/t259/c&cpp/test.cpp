TEST_CASE("Check if a number is a compliant four-digit number", "[is_compliant_four_digit]") {
    REQUIRE(is_compliant_four_digit(1000) == true);
    REQUIRE(is_compliant_four_digit(5678) == true);
    REQUIRE(is_compliant_four_digit(9999) == true);

    REQUIRE(is_compliant_four_digit(999) == false);
    REQUIRE(is_compliant_four_digit(10000) == false);
    REQUIRE(is_compliant_four_digit(-1000) == false);
    REQUIRE(is_compliant_four_digit(123) == false);
}