TEST_CASE("Test Get Mids From Edges") {
    SECTION("Basic Case") {
        std::vector<double> edges = {1, 2, 3, 4};
        std::vector<double> expected_mids = {1.5, 2.5, 3.5};
        REQUIRE(getMidsFromEdges(edges) == expected_mids);
    }

    SECTION("Single Interval") {
        std::vector<double> edges = {5, 10};
        std::vector<double> expected_mids = {7.5};
        REQUIRE(getMidsFromEdges(edges) == expected_mids);
    }

    SECTION("Multiple Intervals") {
        std::vector<double> edges = {0, 1, 2, 3, 4, 5};
        std::vector<double> expected_mids = {0.5, 1.5, 2.5, 3.5, 4.5};
        REQUIRE(getMidsFromEdges(edges) == expected_mids);
    }

    SECTION("Negative Edges") {
        std::vector<double> edges = {-5, -3, -1, 1};
        std::vector<double> expected_mids = {-4.0, -2.0, 0.0};
        REQUIRE(getMidsFromEdges(edges) == expected_mids);
    }

    SECTION("Zero Edges") {
        std::vector<double> edges = {0, 1, 2};
        std::vector<double> expected_mids = {0.5, 1.5};
        REQUIRE(getMidsFromEdges(edges) == expected_mids);
    }

    SECTION("Float Edges") {
        std::vector<double> edges = {0.0, 1.5, 3.0};
        std::vector<double> expected_mids = {0.75, 2.25};
        REQUIRE(getMidsFromEdges(edges) == expected_mids);
    }

    SECTION("Empty Array") {
        std::vector<double> edges = {};
        std::vector<double> expected_mids = {};
        REQUIRE(getMidsFromEdges(edges) == expected_mids);
    }
}