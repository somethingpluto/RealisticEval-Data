TEST_CASE("TestFindClosestElement", "[find_closest_element]") {
    SECTION("test_basic_functionality") {
        REQUIRE(find_closest_element(5, {1, 3, 7, 8, 9}) == Approx(3));
        CHECK("Should return 3 as it is the first closest element to 5");
    }

    SECTION("test_exact_match") {
        REQUIRE(find_closest_element(7, {1, 3, 7, 8, 9}) == Approx(7));
        CHECK("Should return 7 as it exactly matches the target");
    }

    SECTION("test_multiple_closest_values") {
        REQUIRE(find_closest_element(5, {4, 6, 8, 9}) == Approx(4));
        CHECK("Should return 4 as it is the first closest element to 5");
    }

    SECTION("test_float_values") {
        REQUIRE(find_closest_element(5.5, {1.1, 3.3, 7.7, 8.8}) == Approx(3.3));
        CHECK("Should return 3.3 as it is the first closest element to 5.5");
    }
}