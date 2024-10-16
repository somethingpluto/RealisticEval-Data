TEST_CASE("Find T for X at start", "[bezier]") {
    const double TOLERANCE = 1e-6;
    double p0 = 0.0;
    double p1 = 0.5;
    double p2 = 1.0;
    double targetX = 0.0;

    double t = find_t_for_x(targetX, p0, p1, p2);
    REQUIRE(std::abs(t - 0.0) < TOLERANCE);
}

TEST_CASE("Find T for X at end", "[bezier]") {
    const double TOLERANCE = 1e-6;
    double p0 = 0.0;
    double p1 = 0.5;
    double p2 = 1.0;
    double targetX = 1.0;

    double t = find_t_for_x(targetX, p0, p1, p2);
    REQUIRE(std::abs(t - 1.0) < TOLERANCE);
}

TEST_CASE("Find T for X mid curve", "[bezier]") {
    const double TOLERANCE = 1e-6;
    double p0 = 0.0;
    double p1 = 0.5;
    double p2 = 1.0;
    double targetX = 0.25;

    double t = find_t_for_x(targetX, p0, p1, p2);
    REQUIRE(std::abs(t - 0.25) < TOLERANCE);
}

TEST_CASE("Find T for X near mid curve", "[bezier]") {
    const double TOLERANCE = 1e-6;
    double p0 = 0.0;
    double p1 = 1.0;
    double p2 = 2.0;
    double targetX = 1.5;

    double t = find_t_for_x(targetX, p0, p1, p2);
    REQUIRE(std::abs(t - 0.75) < TOLERANCE);
}