TEST_CASE("Test scaling of point clouds", "[scalePointCloud]") {
    SECTION("Test simple scaling") {
        Eigen::MatrixXd pointCloud(1, 3);
        pointCloud << 1.0, 2.0, 3.0;
        double scale_factor = 2.0;
        Eigen::MatrixXd expected_output(1, 3);
        expected_output << 2.0, 4.0, 6.0;

        REQUIRE((scale_point_cloud(pointCloud, scale_factor)).isApprox(expected_output));
    }

    SECTION("Test multiple points scaling") {
        Eigen::MatrixXd pointCloud(2, 3);
        pointCloud << 1.0, 2.0, 3.0,
                      4.0, 5.0, 6.0;
        double scale_factor = 0.5;
        Eigen::MatrixXd expected_output(2, 3);
        expected_output << 0.5, 1.0, 1.5,
                           2.0, 2.5, 3.0;

        REQUIRE((scale_point_cloud(pointCloud, scale_factor)).isApprox(expected_output));
    }

    SECTION("Test zero scaling") {
        Eigen::MatrixXd pointCloud(2, 3);
        pointCloud << 1.0, 2.0, 3.0,
                      4.0, 5.0, 6.0;
        double scale_factor = 0.0;
        Eigen::MatrixXd expected_output(2, 3);
        expected_output << 0.0, 0.0, 0.0,
                           0.0, 0.0, 0.0;

        REQUIRE((scale_point_cloud(pointCloud, scale_factor)).isApprox(expected_output));
    }

    SECTION("Test negative scaling") {
        Eigen::MatrixXd pointCloud(1, 3);
        pointCloud << 1.0, 2.0, 3.0;
        double scale_factor = -2.0;
        Eigen::MatrixXd expected_output(1, 3);
        expected_output << -2.0, -4.0, -6.0;

        REQUIRE((scale_point_cloud(pointCloud, scale_factor)).isApprox(expected_output));
    }
}