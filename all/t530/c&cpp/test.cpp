TEST_CASE("createMatrix", "[matrix]") {
    SECTION("should create a 2x2 matrix filled with zeros") {
        auto result = createMatrix(2, 2, 0);
        REQUIRE(result == std::vector<std::vector<int>>{{0, 0}, {0, 0}});
    }

    SECTION("should create a 3x3 matrix filled with ones") {
        auto result = createMatrix(3, 3, 1);
        REQUIRE(result == std::vector<std::vector<int>>{{1, 1, 1}, {1, 1, 1}, {1, 1, 1}});
    }

    SECTION("should create a 4x5 matrix filled with a string") {
        auto result = createMatrix(4, 5, std::string("test"));
        REQUIRE(result == std::vector<std::vector<std::string>>{
            {"test", "test", "test", "test", "test"},
            {"test", "test", "test", "test", "test"},
            {"test", "test", "test", "test", "test"},
            {"test", "test", "test", "test", "test"},
        });
    }

    SECTION("should create a 0x0 matrix") {
        auto result = createMatrix(0, 0, 0);
        REQUIRE(result == std::vector<std::vector<int>>{});
    }

    SECTION("should create a 1x1 matrix with a boolean") {
        auto result = createMatrix(1, 1, true);
        REQUIRE(result == std::vector<std::vector<bool>>{{true}});
    }

    SECTION("should create a 5x5 matrix filled with negative numbers") {
        auto result = createMatrix(5, 5, -1);
        REQUIRE(result == std::vector<std::vector<int>>{
            {-1, -1, -1, -1, -1},
            {-1, -1, -1, -1, -1},
            {-1, -1, -1, -1, -1},
            {-1, -1, -1, -1, -1},
            {-1, -1, -1, -1, -1},
        });
    }
}