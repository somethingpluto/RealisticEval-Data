TEST_CASE("Test convert_score_to_decimal") {
    SECTION("Test a simple decimal score") {
        REQUIRE(convert_score_to_decimal("2.5").value() == Approx(2.5f));
    }

    SECTION("Test a fraction score") {
        REQUIRE(convert_score_to_decimal("10/4").value() == Approx(2.5f));
    }

    SECTION("Test an integer score represented as a string") {
        REQUIRE(convert_score_to_decimal("5").value() == Approx(5.0f));
    }

    SECTION("Test an integer divide score") {
        REQUIRE(convert_score_to_decimal("12/3").value() == Approx(4.0f));
    }
}