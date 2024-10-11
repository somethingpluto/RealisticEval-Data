TEST_CASE("Probability of Red Balls", "[probability]") {
    REQUIRE(probability_of_red_balls(0, 5, 10) == Approx(0.24609375).epsilon(1e-6));
    REQUIRE(probability_of_red_balls(1, 5, 10) == Approx(0.390625).epsilon(1e-6));
    REQUIRE(probability_of_red_balls(2, 5, 10) == Approx(0.234375).epsilon(1e-6));
    REQUIRE(probability_of_red_balls(3, 5, 10) == Approx(0.0859375).epsilon(1e-6));
    REQUIRE(probability_of_red_balls(4, 5, 10) == Approx(0.0234375).epsilon(1e-6));
    REQUIRE_THROWS(probability_of_red_balls(-1, 5, 10)); // Invalid input
    REQUIRE_THROWS(probability_of_red_balls(6, 5, 10)); // Invalid input
}