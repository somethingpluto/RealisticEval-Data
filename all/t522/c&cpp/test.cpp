#include <catch2/catch_test_macros.hpp>
#include <Eigen/Dense>
#include <cmath>

TEST_CASE("Test Rotate Point Cloud", "[rotate_point_cloud]") {
    SECTION("Test no rotation") {
        Eigen::MatrixXd pointCloud(1, 3);
        pointCloud << 1.0, 2.0, 3.0;
        double rotationAngle = 0;
        Eigen::MatrixXd expectedOutput(1, 3);
        expectedOutput << 1.0, 2.0, 3.0;

        Eigen::MatrixXd rotatedPointCloud = rotatePointCloud(pointCloud, rotationAngle);

        REQUIRE(rotatedPointCloud.isApprox(expectedOutput));
    }

    SECTION("Test 180-degree rotation") {
        Eigen::MatrixXd pointCloud(2, 3);
        pointCloud << 1.0, 0.0, 0.0,
                      0.0, 1.0, 0.0;
        double rotationAngle = M_PI;  // 180 degrees
        Eigen::MatrixXd expectedOutput(2, 3);
        expectedOutput << -1.0, 0.0, 0.0,
                           0.0, 1.0, 0.0;

        Eigen::MatrixXd rotatedPointCloud = rotatePointCloud(pointCloud, rotationAngle);

        REQUIRE(rotatedPointCloud.isApprox(expectedOutput));
    }

    SECTION("Test full rotation") {
        Eigen::MatrixXd pointCloud(1, 3);
        pointCloud << 1.0, 2.0, 3.0;
        double rotationAngle = 2 * M_PI;  // 360 degrees
        Eigen::MatrixXd expectedOutput(1, 3);
        expectedOutput << 1.0, 2.0, 3.0;

        Eigen::MatrixXd rotatedPointCloud = rotatePointCloud(pointCloud, rotationAngle);

        REQUIRE(rotatedPointCloud.isApprox(expectedOutput));
    }
}