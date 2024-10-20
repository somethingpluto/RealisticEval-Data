TEST_CASE("Test valid cases", "[find_powers]") {
    SECTION("Valid numbers with only 2's and 3's as prime factors") {
        CHECK(find_powers(18) == std::make_pair(1, 2));  // 18 = 2^1 * 3^2
        CHECK(find_powers(8) == std::make_pair(3, 0));   // 8 = 2^3 * 3^0
        CHECK(find_powers(27) == std::make_pair(0, 3));  // 27 = 2^0 * 3^3
        CHECK(find_powers(12) == std::make_pair(2, 1));  // 12 = 2^2 * 3^1
        CHECK(find_powers(1) == std::make_pair(0, 0));   // 1 = 2^0 * 3^0
    }
}

TEST_CASE("Test invalid cases", "[find_powers]") {
    SECTION("Numbers with prime factors other than 2 and 3") {
        CHECK(find_powers(7) == std::make_pair(-1, -1));  // 7 is a prime factor
        CHECK(find_powers(14) == std::make_pair(-1, -1)); // 14 = 2^1 * 7^1 (contains 7)
        CHECK(find_powers(10) == std::make_pair(-1, -1)); // 10 = 2^1 * 5^1 (contains 5)
    }
}

TEST_CASE("Test large numbers", "[find_powers]") {
    SECTION("Large numbers that have only 2 and 3 as prime factors") {
        CHECK(find_powers(864) == std::make_pair(5, 3));  // 864 = 2^5 * 3^3
        CHECK(find_powers(729) == std::make_pair(0, 6));  // 729 = 2^0 * 3^6
    }
}

TEST_CASE("Test edge cases", "[find_powers]") {
    SECTION("Edge cases for minimal inputs") {
        CHECK(find_powers(2) == std::make_pair(1, 0));  // 2 = 2^1 * 3^0
        CHECK(find_powers(3) == std::make_pair(0, 1));  // 3 = 2^0 * 3^1
    }
}