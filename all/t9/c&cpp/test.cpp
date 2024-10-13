TEST_CASE("Test Point On Line", "[point_on_line]") {
    SECTION("Point on line") {
        std::vector<int> A = {0, 0};
        std::vector<int> B = {10, 10};
        std::vector<int> C = {5, 5};
        REQUIRE(is_point_on_line(A, B, C));
    }

    SECTION("Point not on line") {
        std::vector<int> A = {0, 0};
        std::vector<int> B = {10, 10};
        std::vector<int> C = {5, 6};
        REQUIRE_FALSE(is_point_on_line(A, B, C));
    }

    SECTION("Vertical line") {
        std::vector<int> A = {5, 0};
        std::vector<int> B = {5, 10};
        std::vector<int> C = {5, 5};
        REQUIRE(is_point_on_line(A, B, C));
    }

    SECTION("Horizontal line") {
        std::vector<int> A = {0, 5};
        std::vector<int> B = {10, 5};
        std::vector<int> C = {5, 5};
        REQUIRE(is_point_on_line(A, B, C));
    }

    SECTION("Point not on vertical line") {
        std::vector<int> A = {5, 0};
        std::vector<int> B = {5, 10};
        std::vector<int> C = {6, 5};
        REQUIRE_FALSE(is_point_on_line(A, B, C));
    }
}