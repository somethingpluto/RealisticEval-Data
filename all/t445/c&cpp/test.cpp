#include <catch2/catch.hpp>
#include <Eigen/Dense>

using namespace Eigen;

// Define the function to create rotation matrices
Matrix4d createRotMatrix(double angleDeg, char axis) {
    double angleRad = angleDeg * M_PI / 180.0;
    Matrix4d rotMat = Matrix4d::Identity();

    switch(axis) {
        case 'X':
            rotMat << 1, 0, 0, 0,
                      0, cos(angleRad), -sin(angleRad), 0,
                      0, sin(angleRad), cos(angleRad), 0,
                      0, 0, 0, 1;
            break;
        case 'Y':
            rotMat << cos(angleRad), 0, sin(angleRad), 0,
                      0, 1, 0, 0,
                      -sin(angleRad), 0, cos(angleRad), 0,
                      0, 0, 0, 1;
            break;
        case 'Z':
            rotMat << cos(angleRad), -sin(angleRad), 0, 0,
                      sin(angleRad), cos(angleRad), 0, 0,
                      0, 0, 1, 0,
                      0, 0, 0, 1;
            break;
        default:
            throw std::invalid_argument("Invalid axis specified");
    }

    return rotMat;
}

TEST_CASE("Create Rotation Matrix", "[rotation]") {
    // Test for X-axis rotation
    auto xRotation = createRotMatrix(90.0, 'X');
    REQUIRE(xRotation(1, 1) == Approx(cos(M_PI / 2)).margin(1e-6));
    REQUIRE(xRotation(1, 2) == Approx(-sin(M_PI / 2)).margin(1e-6));
    REQUIRE(xRotation(2, 1) == Approx(sin(M_PI / 2)).margin(1e-6));
    REQUIRE(xRotation(2, 2) == Approx(cos(M_PI / 2)).margin(1e-6));

    // Test for Y-axis rotation
    auto yRotation = createRotMatrix(90.0, 'Y');
    REQUIRE(yRotation(0, 0) == Approx(cos(M_PI / 2)).margin(1e-6));
    REQUIRE(yRotation(0, 2) == Approx(sin(M_PI / 2)).margin(1e-6));
    REQUIRE(yRotation(2, 0) == Approx(-sin(M_PI / 2)).margin(1e-6));
    REQUIRE(yRotation(2, 2) == Approx(cos(M_PI / 2)).margin(1e-6));

    // Test for Z-axis rotation
    auto zRotation = createRotMatrix(90.0, 'Z');
    REQUIRE(zRotation(0, 0) == Approx(cos(M_PI / 2)).margin(1e-6));
    REQUIRE(zRotation(0, 1) == Approx(-sin(M_PI / 2)).margin(1e-6));
    REQUIRE(zRotation(1, 0) == Approx(sin(M_PI / 2)).margin(1e-6));
    REQUIRE(zRotation(1, 1) == Approx(cos(M_PI / 2)).margin(1e-6));
}
