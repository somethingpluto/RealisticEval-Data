TEST_CASE("TestTranslatePointCloud", "[translatePointCloud]") {
    SECTION("test_simple_translation") {
        // Test a simple translation of a single point
        Eigen::MatrixXd pointCloud(1, 3);
        pointCloud << 1.0, 2.0, 3.0;
        Eigen::RowVector3d translationVector(1.0, 1.0, 1.0);
        Eigen::MatrixXd expectedOutput(1, 3);
        expectedOutput << 2.0, 3.0, 4.0;

        REQUIRE(translate_point_cloud(pointCloud, translationVector).isApprox(expectedOutput));
    }

    SECTION("test_multiple_points_translation") {
        // Test translation of multiple points
        Eigen::MatrixXd pointCloud(2, 3);
        pointCloud << 1.0, 2.0, 3.0,
                      4.0, 5.0, 6.0;
        Eigen::RowVector3d translationVector(1.0, 2.0, 3.0);
        Eigen::MatrixXd expectedOutput(2, 3);
        expectedOutput << 2.0, 4.0, 6.0,
                          5.0, 7.0, 9.0;

        REQUIRE(translate_point_cloud(pointCloud, translationVector).isApprox(expectedOutput));
    }

    SECTION("test_zero_translation") {
        // Test translation by a zero vector (should return the same point cloud)
        Eigen::MatrixXd pointCloud(2, 3);
        pointCloud << 1.0, 2.0, 3.0,
                      4.0, 5.0, 6.0;
        Eigen::RowVector3d translationVector(0.0, 0.0, 0.0);
        Eigen::MatrixXd expectedOutput = pointCloud;  // No change expected

        REQUIRE(translate_point_cloud(pointCloud, translationVector).isApprox(expectedOutput));
    }

    SECTION("test_negative_translation") {
        // Test translation with negative values
        Eigen::MatrixXd pointCloud(1, 3);
        pointCloud << 1.0, 2.0, 3.0;
        Eigen::RowVector3d translationVector(-1.0, -2.0, -3.0);
        Eigen::MatrixXd expectedOutput(1, 3);
        expectedOutput << 0.0, 0.0, 0.0;

        REQUIRE(translate_point_cloud(pointCloud, translationVector).isApprox(expectedOutput));
    }
}