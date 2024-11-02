TEST_CASE("OrthogonalPolynomial - Lanczos Basic Test", "[lanczos]") {
    std::vector<double> x = {0.0, 0.5, 1.0};
    std::vector<double> w = {0.333, 0.333, 0.334};
    QuadratureRule quadrature_rule{x, w};
    int n = 2;

    auto [alpha, beta, gamma, _] = lanczos(n, quadrature_rule);

    REQUIRE(alpha.size() == n);
    REQUIRE(beta.size() == n - 1);
    REQUIRE(gamma.size() == n);
}

TEST_CASE("OrthogonalPolynomial - Lanczos n greater than length", "[lanczos]") {
    std::vector<double> x = {0.0, 0.5, 1.0};
    std::vector<double> w = {0.333, 0.333, 0.334};
    QuadratureRule quadrature_rule{x, w};
    int n = 4;

    REQUIRE_THROWS_AS(lanczos(n, quadrature_rule), std::invalid_argument);
}

TEST_CASE("OrthogonalPolynomial - Lanczos n zero", "[lanczos]") {
    std::vector<double> x = {0.0, 0.5, 1.0};
    std::vector<double> w = {0.333, 0.333, 0.334};
    QuadratureRule quadrature_rule{x, w};
    int n = 0;

    REQUIRE_THROWS_AS(lanczos(n, quadrature_rule), std::invalid_argument);
}

TEST_CASE("OrthogonalPolynomial - Lanczos Weights Nonuniform", "[lanczos]") {
    std::vector<double> x = {0.0, 0.5, 1.0};
    std::vector<double> w = {0.1, 0.4, 0.5};
    QuadratureRule quadrature_rule{x, w};
    int n = 3;

    auto [alpha, beta, gamma, _] = lanczos(n, quadrature_rule);

    REQUIRE(alpha.size() == n);
    REQUIRE(beta.size() == n - 1);
    REQUIRE(gamma.size() == n);

    for (const auto& g : gamma) {
        REQUIRE(g > 0.0);
    }
}

TEST_CASE("OrthogonalPolynomial - Lanczos Single Node", "[lanczos]") {
    std::vector<double> x = {0.5};
    std::vector<double> w = {1.0};
    QuadratureRule quadrature_rule{x, w};
    int n = 1;

    auto [alpha, beta, gamma, _] = lanczos(n, quadrature_rule);

    REQUIRE(alpha.size() == n);
    REQUIRE(beta.size() == n - 1);
    REQUIRE(gamma.size() == n);

    for (const auto& g : gamma) {
        REQUIRE(g > 0.0);
    }
}