#include <catch2/catch_test_macros.hpp>
#include <Eigen/Dense>
#include <stdexcept>

using Eigen::MatrixXd;
TEST_CASE("TestFlipPointCloud", "[FlipPointCloud]") {
    SECTION("test_flip_x_axis") {
        // Test flipping the point cloud across the x-axis.
        MatrixXd pointCloud(2, 3);
        pointCloud << 1.0, 2.0, 3.0,
                      4.0, 5.0, 6.0;

        MatrixXd expectedOutput(2, 3);
        expectedOutput << 1.0, -2.0, 3.0,
                         4.0, -5.0, 6.0;

        MatrixXd flippedPointCloud = flipPointCloud(pointCloud, 1);
        REQUIRE(flippedPointCloud.isApprox(expectedOutput));
    }

    SECTION("test_flip_y_axis") {
        // Test flipping the point cloud across the y-axis.
        MatrixXd pointCloud(2, 3);
        pointCloud << 1.0, 2.0, 3.0,
                      4.0, 5.0, 6.0;

        MatrixXd expectedOutput(2, 3);
        expectedOutput << -1.0, 2.0, 3.0,
                          -4.0, 5.0, 6.0;

        MatrixXd flippedPointCloud = flipPointCloud(pointCloud, 0);
        REQUIRE(flippedPointCloud.isApprox(expectedOutput));
    }

    SECTION("test_flip_z_axis") {
        // Test flipping the point cloud across the z-axis.
        MatrixXd pointCloud(2, 3);
        pointCloud << 1.0, 2.0, 3.0,
                      4.0, 5.0, 6.0;

        MatrixXd expectedOutput(2, 3);
        expectedOutput << 1.0, 2.0, -3.0,
                         4.0, 5.0, -6.0;

        MatrixXd flippedPointCloud = flipPointCloud(pointCloud, 2);
        REQUIRE(flippedPointCloud.isApprox(expectedOutput));
    }

    SECTION("test_invalid_axis") {
        // Test handling of an invalid axis.
        MatrixXd pointCloud(1, 3);
        pointCloud << 1.0, 2.0, 3.0;

        REQUIRE_THROWS_AS(flipPointCloud(pointCloud, 3), std::invalid_argument);
    }

    SECTION("test_empty_point_cloud") {
        // Test flipping an empty point cloud.
        MatrixXd pointCloud(0, 3);
        MatrixXd expectedOutput(0, 3);

        MatrixXd flippedPointCloud = flipPointCloud(pointCloud, 0);
        REQUIRE(flippedPointCloud.rows() == expectedOutput.rows());
        REQUIRE(flippedPointCloud.cols() == expectedOutput.cols());
    }
}