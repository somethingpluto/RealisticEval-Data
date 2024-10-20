TEST_CASE("Create Rotation Matrix", "[rotation]") {
    // Test for X-axis rotation
    auto xRotation = create_rot_matrix(90.0, 'X');
    REQUIRE(xRotation(1, 1) == Approx(cos(M_PI / 2)).margin(1e-6));
    REQUIRE(xRotation(1, 2) == Approx(-sin(M_PI / 2)).margin(1e-6));
    REQUIRE(xRotation(2, 1) == Approx(sin(M_PI / 2)).margin(1e-6));
    REQUIRE(xRotation(2, 2) == Approx(cos(M_PI / 2)).margin(1e-6));

    // Test for Y-axis rotation
    auto yRotation = create_rot_matrix(90.0, 'Y');
    REQUIRE(yRotation(0, 0) == Approx(cos(M_PI / 2)).margin(1e-6));
    REQUIRE(yRotation(0, 2) == Approx(sin(M_PI / 2)).margin(1e-6));
    REQUIRE(yRotation(2, 0) == Approx(-sin(M_PI / 2)).margin(1e-6));
    REQUIRE(yRotation(2, 2) == Approx(cos(M_PI / 2)).margin(1e-6));

    // Test for Z-axis rotation
    auto zRotation = create_rot_matrix(90.0, 'Z');
    REQUIRE(zRotation(0, 0) == Approx(cos(M_PI / 2)).margin(1e-6));
    REQUIRE(zRotation(0, 1) == Approx(-sin(M_PI / 2)).margin(1e-6));
    REQUIRE(zRotation(1, 0) == Approx(sin(M_PI / 2)).margin(1e-6));
    REQUIRE(zRotation(1, 1) == Approx(cos(M_PI / 2)).margin(1e-6));
}
