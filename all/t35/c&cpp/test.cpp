#define CATCH_CONFIG_MAIN  // This tells Catch to provide a main() - only do this in one cpp file
#include <catch2/catch.hpp>
#include <vector>
#include <tuple>

// Forward declaration of the function to be tested
bool is_point_in_polygon(std::tuple<double, double> point, const std::vector<std::tuple<double, double>>& polygon);

TEST_CASE("is_point_in_polygon tests") {
    // Define the polygons to be used in tests
    std::vector<std::tuple<double, double>> square = {{0, 0}, {0, 10}, {10, 10}, {10, 0}};
    std::vector<std::tuple<double, double>> triangle = {{0, 0}, {5, 10}, {10, 0}};
    std::vector<std::tuple<double, double>> concave = {{0, 0}, {5, 5}, {10, 0}, {5, 10}, {0, 10}};

    SECTION("Point inside the square") {
        REQUIRE(is_point_in_polygon(std::make_tuple(5, 5), square) == true);
    }

    SECTION("Point outside the square") {
        REQUIRE(is_point_in_polygon(std::make_tuple(15, 5), square) == false);
    }

    SECTION("Point on the edge of the triangle") {
        // Depending on the implementation detail, the behavior of points on the edge may differ
        REQUIRE(is_point_in_polygon(std::make_tuple(5, 0), triangle) == false);
    }

    SECTION("Point inside concave polygon") {
        REQUIRE(is_point_in_polygon(std::make_tuple(5, 9), concave) == true);
    }

    SECTION("Point outside concave polygon") {
        REQUIRE(is_point_in_polygon(std::make_tuple(5, 1), concave) == false);
    }
}