TEST_CASE("Node Test Cases", "[Node]") {
    // Test Case 1: 2 players (smallest valid case)
    Node game1(2);
    REQUIRE(game1.startGame() == 2);

    // Test Case 2: 3 players
    Node game2(3);
    REQUIRE(game2.startGame() == 3);

    // Test Case 3: 5 players
    Node game3(5);
    REQUIRE(game3.startGame() == 3);

    // Test Case 4: 7 players
    Node game4(7);
    REQUIRE(game4.startGame() == 4);

    // Test Case 5: 10 players
    Node game5(10);
    REQUIRE(game5.startGame() == 8);
}