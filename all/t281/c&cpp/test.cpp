TEST_CASE("Squared Euclidean Distance", "[squared_euclidean_distance]") {
    SECTION("Equal Vectors") {
        std::vector<int> vec1 = {1, 2, 3};
        std::vector<int> vec2 = {1, 2, 3};
        REQUIRE(squared_euclidean_distance(vec1, vec2) == 0);
    }

    SECTION("Different Vectors") {
        std::vector<int> vec1 = {1, 2, 3};
        std::vector<int> vec2 = {4, 5, 6};
        REQUIRE(squared_euclidean_distance(vec1, vec2) == 27);
    }

    SECTION("Empty Vectors") {
        std::vector<int> vec1 = {};
        std::vector<int> vec2 = {};
        REQUIRE(squared_euclidean_distance(vec1, vec2) == 0);
    }

    SECTION("Single Element Vectors") {
        std::vector<int> vec1 = {1};
        std::vector<int> vec2 = {2};
        REQUIRE(squared_euclidean_distance(vec1, vec2) == 1);
    }

    SECTION("Vectors with Negative Elements") {
        std::vector<int> vec1 = {-1, -2, -3};
        std::vector<int> vec2 = {1, 2, 3};
        REQUIRE(squared_euclidean_distance(vec1, vec2) == 36);
    }

    SECTION("Vectors of Different Sizes Should Throw Exception") {
        std::vector<int> vec1 = {1, 2, 3};
        std::vector<int> vec2 = {1, 2};
        REQUIRE_THROWS_WITH(squared_euclidean_distance(vec1, vec2), "Vectors must be of the same size");
    }
}