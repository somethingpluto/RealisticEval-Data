TEST_CASE("Simpson's Rule Tests") {

    SECTION("Basic Integral of x^2 from 0 to 1") {
        // The exact integral of f(x) = x^2 from 0 to 1 is 1/3
        double result = simpsons_rule(0.0, 1.0, 10);
        REQUIRE(result == Approx(1.0 / 3.0).epsilon(0.01));
    }

    SECTION("Basic Integral of x^2 from 0 to 2") {
        // The exact integral of f(x) = x^2 from 0 to 2 is 8/3
        double result = simpsons_rule(0.0, 2.0, 10);
        REQUIRE(result == Approx(8.0 / 3.0).epsilon(0.01));
    }

    SECTION("Negative Integral of x^2 from -1 to 0") {
        // The exact integral of f(x) = x^2 from -1 to 0 is 1/3
        double result = simpsons_rule(-1.0, 0.0, 10);
        REQUIRE(result == Approx(1.0 / 3.0).epsilon(0.01));
    }

    SECTION("Large Interval") {
        // Test with a larger interval from 0 to 10
        double result = simpsons_rule(0.0, 10.0, 20);
        // The exact integral from 0 to 10 of f(x) = x^2 is (10^3)/3 = 1000/3
        REQUIRE(result == Approx(1000.0 / 3.0).epsilon(0.01));
    }
}