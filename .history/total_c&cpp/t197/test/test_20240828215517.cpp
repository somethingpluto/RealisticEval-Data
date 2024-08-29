TEST_CASE("PrimeGame Test Cases", "[PrimeGame]") {
    // Test Case 1: 2 players (smallest valid case)
    PrimeGame game1(2);
    REQUIRE(game1.startGame() == 2);

    // Test Case 2: 3 players
    PrimeGame game2(3);
    REQUIRE(game2.startGame() == 3);

    // Test Case 3: 5 players
    PrimeGame game3(5);
    REQUIRE(game3.startGame() == 3);

    // Test Case 4: 7 players
    PrimeGame game4(7);
    REQUIRE(game4.startGame() == 4);

    // Test Case 5: 10 players
    PrimeGame game5(10);
    REQUIRE(game5.startGame() == 8);
}