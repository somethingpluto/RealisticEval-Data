TEST_CASE("Test Probability Red Balls") {
    SECTION("All balls are red") {
        REQUIRE(probability_red_balls(5, 5, 0) == Approx(1));
    }

    SECTION("No red balls are available") {
        REQUIRE(probability_red_balls(1, 0, 5) == Approx(0));
    }

    SECTION("Typical scenario") {
        REQUIRE(probability_red_balls(2, 10, 5) == Approx(static_cast<double>(binomial_coefficient(10, 2)) / binomial_coefficient(15, 2)));
    }

    SECTION("More balls requested than available") {
        REQUIRE(probability_red_balls(6, 5, 4) == Approx(0));
    }

    SECTION("High combinations") {
        REQUIRE(probability_red_balls(3, 20, 30) == Approx(static_cast<double>(binomial_coefficient(20, 3)) / binomial_coefficient(50, 3)));
    }
}