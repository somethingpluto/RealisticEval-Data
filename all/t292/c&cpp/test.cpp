TEST_CASE("calculateRemainingPayment") {
    SECTION("calculates remaining balance for typical loan conditions") {
        REQUIRE(calculateRemainingPayment(10000, 0.005, 24) == Catch::Approx(0).margin(0.01));
    }

    SECTION("calculates remaining balance for high interest rate") {
        REQUIRE(calculateRemainingPayment(10000, 0.1, 12) == Catch::Approx(0).margin(0.01));
    }

    SECTION("calculates remaining balance for low interest rate") {
        REQUIRE(calculateRemainingPayment(10000, 0.001, 60) == Catch::Approx(0).margin(0.01));
    }

    SECTION("calculates remaining balance for very short term") {
        REQUIRE(calculateRemainingPayment(10000, 0.005, 1) == Catch::Approx(0).margin(0.01));
    }

    SECTION("calculates remaining balance with no payments") {
        REQUIRE(calculateRemainingPayment(10000, 0.005, 0) == Catch::Approx(10000).margin(0.01));
    }

    SECTION("calculates remaining balance for a long term") {
        REQUIRE(calculateRemainingPayment(10000, 0.005, 360) == Catch::Approx(0).margin(0.01));
    }
}