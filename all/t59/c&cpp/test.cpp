TEST_CASE("Probability of drawing red balls", "[probability]") {
    REQUIRE(probability_red_balls(0, 5, 3) == Approx(1.0)); // No balls drawn, so the probability is 1
    REQUIRE(probability_red_balls(1, 5, 3) == Approx(0.625)); // Drawing 1 red ball out of 8 total
    REQUIRE(probability_red_balls(2, 5, 3) == Approx(0.1875)); // Drawing 2 red balls out of 8 total
    REQUIRE(probability_red_balls(3, 5, 3) == Approx(0.0416667)); // Drawing 3 red balls out of 8 total
    REQUIRE(probability_red_balls(4, 5, 3) == Approx(0.0)); // Not possible to draw 4 red balls with only 5 red balls

    // Additional edge cases
    REQUIRE(probability_red_balls(-1, 5, 3) == Approx(0.0)); // Invalid number of balls to draw
    REQUIRE(probability_red_balls(6, 5, 3) == Approx(0.0)); // Drawing more balls than available
}
