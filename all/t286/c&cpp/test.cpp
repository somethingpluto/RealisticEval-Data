TEST_CASE("TestFindLargestDivisible", "[find_largest_divisible]") {
    SECTION("test_typical_case") {
        // Test with a typical input where the largest divisible number should be found.
        REQUIRE(find_largest_divisible(50) == 50);
        REQUIRE(find_largest_divisible(47) == 45);
    }

    SECTION("test_no_divisible_found") {
        // Test a case where no divisible number is found within the range.
        REQUIRE(!find_largest_divisible(4).has_value());
    }

    SECTION("test_exact_half_divisible") {
        // Test when the half of n is exactly divisible by 5.
        REQUIRE(find_largest_divisible(10) == 10);
    }

    SECTION("test_large_number") {
        // Test with a large number to ensure performance and correctness.
        REQUIRE(find_largest_divisible(1000) == 1000);
    }

    SECTION("test_lower_bound") {
        // Test the function with the lowest bound that should find a divisible number.
        REQUIRE(find_largest_divisible(5) == 5);
    }
}