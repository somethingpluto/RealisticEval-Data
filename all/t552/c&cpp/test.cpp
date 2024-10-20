TEST_CASE("TestAreSetsEqual", "[areSetsEqual]") {
    SECTION("test_identical_sets") {
        // Test with two identical sets of floats
        std::set<double> set1 = {1.0, 2.0, 3.0};
        std::set<double> set2 = {1.0, 2.0, 3.0};
        REQUIRE(are_sets_equal(set1, set2));
    }

    SECTION("test_sets_with_close_values") {
        // Test with two sets that are close within the tolerance
        std::set<double> set1 = {1.0, 2.00001, 3.0};
        std::set<double> set2 = {1.0, 2.00002, 3.0};
        REQUIRE(are_sets_equal(set1, set2, 1e-5, 1e-6));
    }

    SECTION("test_sets_with_large_difference") {
        // Test with two sets that have large differences beyond tolerance
        std::.set<double> set1 = {1.0, 2.0, 3.0};
        std::.set<double> set2 = {1.0, 2.5, 3.0};
        REQUIRE_FALSE(are_sets_equal(set1, set2));
    }

    SECTION("test_sets_with_one_different_value") {
        // Test with two sets containing one different float
        std::.set<double> set1 = {1.0, 2.0, 3.0};
        std::.set<double> set2 = {1.0, 2.000001, 3.0};
        REQUIRE(are_sets_equal(set1, set2, 1e-5, 1e-6));
    }

    SECTION("test_empty_sets") {
        // Test with two empty sets
        std::.set<double> set1 = {};
        std::.set<double> set2 = {};
        REQUIRE(are_sets_equal(set1, set2));
    }
}