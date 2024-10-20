TEST_CASE("Flatten array tests") {

    // Test a deeply nested array
    SECTION("deeply_nested_array") {
        std::vector<std::vector<int>> nested_array = {{1}, {2, {3, {4, {5}}}}};
        std::vector<int> expected_result = {1, 2, 3, 4, 5};
        REQUIRE(flatten_array(nested_array) == expected_result);
    }

    // Test an array with mixed types (simulated with integers for simplicity)
    SECTION("mixed_types") {
        std::vector<std::vector<int>> mixed_array = {{1}, {2, {3, {4, {5}}}}, {6}};
        std::vector<int> expected_result = {1, 2, 3, 4, 5, 6};
        REQUIRE(flatten_array(mixed_array) == expected_result);
    }

    // Test an empty array
    SECTION("empty_array") {
        std::vector<std::vector<int>> empty_array = {};
        std::vector<int> expected_result = {};
        REQUIRE(flatten_array(empty_array) == expected_result);
    }

    // Test an array that includes empty subarrays
    SECTION("array_with_empty_subarrays") {
        std::vector<std::vector<int>> complex_array = {{1}, {}, {2, {}, 3}, {4, {5, {}, 6}, 7}, {}};
        std::vector<int> expected_result = {1, 2, 3, 4, 5, 6, 7};
        REQUIRE(flatten_array(complex_array) == expected_result);
    }

    // Test an array that has no nested structure
    SECTION("no_nested_array") {
        std::vector<std::vector<int>> flat_array = {{1}, {2}, {3}, {4}, {5}};
        std::vector<int> expected_result = {1, 2, 3, 4, 5};
        REQUIRE(flatten_array(flat_array) == expected_result);
    }
}