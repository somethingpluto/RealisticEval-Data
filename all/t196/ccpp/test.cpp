TEST_CASE("Sieve of Eratosthenes Test Cases", "[generatePrimes]") {
    // Test Case 1: Small limit (10)
    std::vector<int> expected1 = {2, 3, 5, 7};
    REQUIRE(generatePrimes(10) == expected1);

    // Test Case 2: Prime limit (29)
    std::vector<int> expected2 = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29};
    REQUIRE(generatePrimes(29) == expected2);

    // Test Case 3: Non-prime limit (30)
    std::vector<int> expected3 = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29};
    REQUIRE(generatePrimes(30) == expected3);

    // Test Case 4: Limit of 2 (smallest prime)
    std::vector<int> expected4 = {2};
    REQUIRE(generatePrimes(2) == expected4);

    // Test Case 5: Invalid limit (1, should throw an exception)
    REQUIRE_THROWS_AS(generatePrimes(1), std::invalid_argument);
}