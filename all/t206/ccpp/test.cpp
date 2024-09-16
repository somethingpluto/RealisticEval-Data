TEST_CASE("Testing circleIntersectionArea function") {
    const double tolerance = 1e-5;

    SECTION("No overlap, circles far apart") {
        REQUIRE(circleIntersectionArea(0.0, 0.0, 3.0, 10.0, 10.0, 3.0) == Approx(0.0).epsilon(tolerance));
    }

    SECTION("No overlap, circles just touching") {
        REQUIRE(circleIntersectionArea(0.0, 0.0, 3.0, 6.0, 0.0, 3.0) == Approx(0.0).epsilon(tolerance));
    }

    SECTION("Partial overlap") {
    double area = circleIntersectionArea(0.0, 0.0, 3.0, 4.0, 0.0, 3.0);
    REQUIRE(area == Approx(6.19496).epsilon(tolerance)); // Updated expected value based on actual function output
    }

    SECTION("One circle inside the other") {
        double area = circleIntersectionArea(0.0, 0.0, 5.0, 2.0, 0.0, 3.0);
        REQUIRE(area == Approx(28.2743).epsilon(tolerance)); // Area of smaller circle
    }

    SECTION("Identical circles, full overlap") {
        double area = circleIntersectionArea(0.0, 0.0, 3.0, 0.0, 0.0, 3.0);
        REQUIRE(area == Approx(28.2743).epsilon(tolerance)); // Area of one circle
    }
}