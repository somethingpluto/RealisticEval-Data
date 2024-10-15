TEST_CASE("calculateDiscount", "[discount]") {
    SECTION("should return 25.00% discount for original price of 100 and actual price of 75") {
        REQUIRE(calculateDiscount(100, 75) == Approx(25.00).margin(0.01));
    }

    SECTION("should return 0.00% discount for original price of 50 and actual price of 50") {
        REQUIRE(calculateDiscount(50, 50) == Approx(0.00).margin(0.01));
    }

    SECTION("should return 100.00% discount for original price of 100 and actual price of 0") {
        REQUIRE(calculateDiscount(100, 0) == Approx(100.00).margin(0.01));
    }

    SECTION("should return 50.00% discount for original price of 200 and actual price of 100") {
        REQUIRE(calculateDiscount(200, 100) == Approx(50.00).margin(0.01));
    }
}