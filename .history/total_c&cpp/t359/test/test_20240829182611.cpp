
TEST_CASE("TrapezoidalRule Test Cases", "[trapezoidal_rule]") {
    // Test Case 1: Integration of a constant function (f(x) = 1) over [0, 1]
    REQUIRE(trapezoidal_rule([](double x) { return 1.0; }, 0.0, 1.0, 100) == Approx(1.0).epsilon(1e-6));

    // Test Case 2: Integration of a linear function (f(x) = x) over [0, 1]
    REQUIRE(trapezoidal_rule([](double x) { return x; }, 0.0, 1.0, 100) == Approx(0.5).epsilon(1e-6));

    // Test Case 3: Integration of a quadratic function (f(x) = x^2) over [0, 1]
    REQUIRE(trapezoidal_rule([](double x) { return x * x; }, 0.0, 1.0, 1000) == Approx(1.0 / 3.0).epsilon(1e-6));

    // Test Case 4: Integration of the sine function (f(x) = sin(x)) over [0, π]
    REQUIRE(trapezoidal_rule([](double x) { return std::sin(x); }, 0.0, M_PI, 1000) == Approx(2.0).epsilon(1e-6));

    // Test Case 5: Integration of an exponential function (f(x) = exp(x)) over [0, 1]
    REQUIRE(trapezoidal_rule([](double x) { return std::exp(x); }, 0.0, 1.0, 100) == Approx(std::exp(1.0) - 1.0).epsilon(1e-6));
}