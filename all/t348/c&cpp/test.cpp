TEST_CASE("TestFindPrimesInRange") {
    SECTION("Find primes in range") {
        std::vector<int> expected = {2, 3, 5, 7, 11};
        REQUIRE(find_primes(1, 12) == expected);
    }

    SECTION("Find primes for a single prime") {
        std::vector<int> expected = {29};
        REQUIRE(find_primes(29, 29) == expected);
    }

    SECTION("Find primes in a large range") {
        std::vector<int> expected = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97};
        REQUIRE(find_primes(1, 100) == expected);
    }

    SECTION("Find primes in a range with no primes") {
        std::vector<int> expected = {};
        REQUIRE(find_primes(0, 1) == expected);
    }
}