#define CATCH_CONFIG_MAIN
#include "catch.hpp"
#include "get_scale.h"  // Include the header where get_scale is defined

TEST_CASE("Test get_scale function", "[get_scale]") {
    Eigen::Matrix3d matrix;

    SECTION("Identity matrix") {
        matrix << 1, 0, 0,
                  0, 1, 0,
                  0, 0, 1;
        auto [scale_x, scale_y] = get_scale(matrix);
        REQUIRE(scale_x == Approx(1.0));
        REQUIRE(scale_y == Approx(1.0));
    }

    SECTION("Scaling matrix along x-axis") {
        matrix << 2, 0, 0,
                  0, 1, 0,
                  0, 0, 1;
        auto [scale_x, scale_y] = get_scale(matrix);
        REQUIRE(scale_x == Approx(2.0));
        REQUIRE(scale_y == Approx(1.0));
    }

    SECTION("Scaling matrix along y-axis") {
        matrix << 1, 0, 0,
                  0, 3, 0,
                  0, 0, 1;
        auto [scale_x, scale_y] = get_scale(matrix);
        REQUIRE(scale_x == Approx(1.0));
        REQUIRE(scale_y == Approx(3.0));
    }

    SECTION("Scaling matrix along both axes") {
        matrix << 2, 0, 0,
                  0, 3, 0,
                  0, 0, 1;
        auto [scale_x, scale_y] = get_scale(matrix);
        REQUIRE(scale_x == Approx(2.0));
        REQUIRE(scale_y == Approx(3.0));
    }
}
