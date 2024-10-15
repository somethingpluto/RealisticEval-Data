TEST_CASE("incrementNumber") {
    REQUIRE(incrementNumber(5) == 6);
    REQUIRE(incrementNumber(0) == 0);
    REQUIRE(incrementNumber(-3) == -3);
    REQUIRE(incrementNumber(0.5) == 1.5);
    REQUIRE(incrementNumber(1) == 2);
    REQUIRE(incrementNumber(-1) == -1);
}