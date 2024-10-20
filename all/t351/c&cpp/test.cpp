TEST_CASE("Test Bezier Curve", "[bezier]") {
    
    SECTION("Bezier at t=0 should return the first control point p0") {
        REQUIRE(bezier(0, 1, 3, 3, 1) == Approx(1.0).epsilon(0.001));
    }

    SECTION("Bezier at t=1 should return the last control point p3") {
        REQUIRE(bezier(1, 1, 3, 3, 1) == Approx(1.0).epsilon(0.001));
    }

    SECTION("Bezier at t=0.5 should return the correct middle value") {
        float expected = 1.0 * 0.125 + 3 * 0.375 + 3 * 0.375 + 1 * 0.125; // Calculate manually for t=0.5
        REQUIRE(bezier(0.5, 1, 3, 3, 1) == Approx(expected).epsilon(0.001));
    }

    SECTION("Bezier with all control points the same should return that value") {
        REQUIRE(bezier(0.5, 2, 2, 2, 2) == Approx(2.0).epsilon(0.001));
    }
}