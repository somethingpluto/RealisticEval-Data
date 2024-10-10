TEST_CASE("Test get_3d_coordinates", "[get_3d_coordinates]") {
    // Test data
    Matrix3d K = Matrix3d::Identity();
    K(0, 0) = 500.0; // fx
    K(1, 1) = 500.0; // fy
    K(0, 2) = 320.0; // cx
    K(1, 2) = 240.0; // cy
    double d = 10.0;  // depth
    double x = 300.0; // pixel x coordinate
    double y = 200.0; // pixel y coordinate

    // Expected result
    Vector3d expected_result(200.0, 160.0, 10.0);

    // Actual result
    Vector3d actual_result = get_3d_coordinates(K, d, x, y);

    // Check if the results match within a small tolerance
    REQUIRE(actual_result.isApprox(expected_result, 1e-6));
}