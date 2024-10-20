TEST_CASE("Change Reference Frame") {
    // Initializing the point cloud and reference frame points
    Eigen::MatrixXd pointCloud(3, 3);
    pointCloud << 1, 2, 3,
                  4, 5, 6,
                  7, 8, 9;

    SECTION("Identity Transformation") {
        std::vector<Eigen::Vector3d> refFramePoints = {
            {0, 0, 0}, 
            {1, 0, 0}, 
            {0, 1, 0}
        };
        Eigen::MatrixXd result = changeReferenceFrame(pointCloud, refFramePoints);
        Eigen::MatrixXd expected = pointCloud; // Expect the same because identity
        REQUIRE((result - expected).norm() < 1e-9); // Use a small tolerance for floating-point comparison
    }

    SECTION("Translation") {
        std::vector<Eigen::Vector3d> framePoints = {
            {1, 1, 1}, 
            {2, 1, 1}, 
            {1, 2, 1}
        };
        Eigen::MatrixXd result = changeReferenceFrame(pointCloud, framePoints);
        Eigen::MatrixXd expected(3, 3);
        expected << -1.0, 0.0, 1.0,
                    2.0, 3.0, 4.0,
                    5.0, 6.0, 7.0;
        REQUIRE((result - expected).norm() < 1e-9);
    }

    SECTION("Rotation") {
        std::vector<Eigen::Vector3d> framePoints = {
            {0, 0, 0}, 
            {0, 1, 0}, 
            {0, 1, 1}
        };
        Eigen::MatrixXd result = changeReferenceFrame(pointCloud, framePoints);
        Eigen::MatrixXd expected(3, 3);
        expected << 2.0, 3.0, 1.0,
                    5.0, 6.0, 4.0,
                    8.0, 9.0, 7.0;
        REQUIRE((result - expected).norm() < 1e-9);
    }

    SECTION("Non-Orthonormal Frame") {
        std::vector<Eigen::Vector3d> framePoints = {
            {0, 0, 0},
            {1, 0, 0},
            {1, 1, 0}
        };
        Eigen::Vector3d u = {1, 0, 0};
        Eigen::Vector3d v = {0, 1, 0};
        Eigen::Vector3d w = u.cross(v);
        Eigen::Matrix3d rotationMatrix;
        rotationMatrix.col(0) = u;
        rotationMatrix.col(1) = v;
        rotationMatrix.col(2) = w;
        
        Eigen::MatrixXd result = changeReferenceFrame(pointCloud, framePoints);
        Eigen::MatrixXd expected = pointCloud * rotationMatrix.transpose();
        REQUIRE((result - expected).norm() < 1e-9);
    }

    SECTION("Inverted Frame") {
        std::vector<Eigen::Vector3d> framePoints = {
            {0, 0, 0},
            {-1, 0, 0},
            {0, -1, 0}
        };
        Eigen::MatrixXd rotationMatrix(3, 3);
        rotationMatrix << -1, 0, 0,
                          0, -1, 0,
                          0, 0, 1;

        Eigen::MatrixXd result = changeReferenceFrame(pointCloud, framePoints);
        Eigen::MatrixXd expected = pointCloud * rotationMatrix;
        REQUIRE((result - expected).norm() < 1e-9);
    }
}