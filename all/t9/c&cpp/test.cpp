TEST_CASE("Test is_point_on_line functionality") {
    SECTION("Point on the line") {
        std::vector<int> A = {0, 0};
        std::vector<int> B = {10, 10};
        std::vector<int> C = {5, 5};
        REQUIRE(is_point_on_line(A, B, C));
    }

    SECTION("Point not on the line") {
        std::vector<int> A = {0, 0};
        std::vector<int> B = {10, 10};
        std::vector<int> C = {5, 6};
        REQUIRE_FALSE(is_point_on_line(A, B, C));
    }

    SECTION("Point on a vertical line") {
        std::vector<int> A = {5, 0};
        std::vector<int> B = {5, 10};
        std::vector<int> C = {5, 5};
        REQUIRE(is_point_on_line(A, B, C));
    }

    SECTION("Point on a horizontal line") {
        std::vector<int> A = {0, 5};
        std::vector<int> B = {10, 5};
        std::vector<int> C = {5, 5};
        REQUIRE(is_point_on_line(A, B, C));
    }

    SECTION("Point not on a vertical line") {
        std::vector<int> A = {5, 0};
        std::vector<int> B = {5, 10};
        std::vector<int> C = {6, 5};
        REQUIRE_FALSE(is_point_on_line(A, B, C));
    }
}