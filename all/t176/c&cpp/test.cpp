TEST_CASE("Find k nearest neighbors simple case") {
    std::vector<Point> points = {
        Point(1, 2),
        Point(3, 4),
        Point(1, -1),
        Point(5, 2)
    };
    Point query_point(2, 2);
    int k = 2;
    auto result = find_k_nearest_neighbors(points, query_point, k);

    REQUIRE(result.size() == 2);
    REQUIRE(contains_point(result, Point(1, 2)));
    REQUIRE(contains_point(result, Point(3, 4)));
}

TEST_CASE("Find k nearest neighbors exact match") {
    std::vector<Point> points = {
        Point(1, 2),
        Point(2, 2),
        Point(3, 3)
    };
    Point query_point(2, 2);
    int k = 1;
    auto result = find_k_nearest_neighbors(points, query_point, k);

    REQUIRE(result.size() == 1);
    REQUIRE(std::fabs(result[0].x - 2.0) < 0.001);
    REQUIRE(std::fabs(result[0].y - 2.0) < 0.001);
}

TEST_CASE("Find k nearest neighbors larger k") {
    std::vector<Point> points = {
        Point(1, 2),
        Point(3, 4),
        Point(1, -1),
        Point(5, 2)
    };
    Point query_point(2, 2);
    int k = 5; // k is larger than the number of points
    auto result = find_k_nearest_neighbors(points, query_point, k);

    REQUIRE(result.size() == 4);
}

TEST_CASE("Find k nearest neighbors empty points") {
    std::vector<Point> points = {};
    Point query_point(2, 2);
    int k = 3;
    auto result = find_k_nearest_neighbors(points, query_point, k);

    REQUIRE(result.size() == 0);
}

TEST_CASE("Find k nearest neighbors all points equidistant") {
    std::vector<Point> points = {
        Point(2, 3),
        Point(3, 2),
        Point(1, 2),
        Point(2, 1)
    };
    Point query_point(2, 2);
    int k = 2;
    auto result = find_k_nearest_neighbors(points, query_point, k);

    REQUIRE(result.size() == 2);
    REQUIRE(contains_point(result, Point(2, 3)));
    REQUIRE(contains_point(result, Point(3, 2)));
}