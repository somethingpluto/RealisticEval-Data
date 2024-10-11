TEST_CASE("applyOp function tests") {
    SECTION("Addition") {
        REQUIRE(applyOp(3, 4, '+') == 7);
        REQUIRE(applyOp(-1, -1, '+') == -2);
    }

    SECTION("Subtraction") {
        REQUIRE(applyOp(10, 5, '-') == 5);
        REQUIRE(applyOp(5, 10, '-') == -5);
    }

    SECTION("Multiplication") {
        REQUIRE(applyOp(3, 4, '*') == 12);
        REQUIRE(applyOp(-2, 5, '*') == -10);
    }

    SECTION("Division") {
        REQUIRE(applyOp(8, 4, '/') == 2);
        REQUIRE(applyOp(5, 2, '/') == 2.5);
        REQUIRE_THROWS_AS(applyOp(5, 0, '/'), std::invalid_argument);
    }

    SECTION("Exponentiation") {
        REQUIRE(applyOp(2, 3, '^') == 8);
        REQUIRE(applyOp(9, 0.5, '^') == 3); // Square root of 9
    }
}