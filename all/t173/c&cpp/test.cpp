TEST_CASE("Cubic Bezier Curve Tests") {
    std::array<double, 2> p0 = {0.0, 0.0};
    std::array<double, 2> p1 = {0.0, 1.0};
    std::array<double, 2> p2 = {1.0, 1.0};
    std::array<double, 2> p3 = {1.0, 0.0};

    SECTION("t = 0.0") {
        double t = 0.0;
        std::array<double, 2> expected = {0.0, 0.0};
        REQUIRE(cubicBezier(t, p0, p1, p2, p3) == expected);
    }

    SECTION("t = 1.0") {
        double t = 1.0;
        std::array<double, 2> expected = {1.0, 0.0};
        REQUIRE(cubicBezier(t, p0, p1, p2, p3) == expected);
    }

    SECTION("t = 0.5") {
        double t = 0.5;
        std::array<double, 2> expected = {0.5, 0.75};
        REQUIRE_THAT(cubicBezier(t, p0, p1, p2, p3), Catch::Equals(expected, 1e-9));
    }

    SECTION("Mid point") {
        std::array<double, 2> p1 = {1.0, 1.0};
        std::array<double, 2> p2 = {2.0, 1.0};
        std::array<double, 2> p3 = {3.0, 0.0};
        double t = 0.5;
        std::array<double, 2> expected = {1.5, 0.75};
        REQUIRE_THAT(cubicBezier(t, p0, p1, p2, p3), Catch::Equals(expected, 1e-9));
    }

    SECTION("Arbitrary t = 0.75") {
        std::array<double, 2> p1 = {0.0, 2.0};
        std::array<double, 2> p2 = {2.0, 2.0};
        std::array<double, 2> p3 = {2.0, 0.0};
        double t = 0.75;
        std::array<double, 2> expected = {1.6875, 1.125};
        REQUIRE_THAT(cubicBezier(t, p0, p1, p2, p3), Catch::Equals(expected, 1e-9));
    }
}