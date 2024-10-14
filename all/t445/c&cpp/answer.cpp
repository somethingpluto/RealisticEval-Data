#include <Eigen/Dense>
#include <cmath>

Eigen::Matrix4d createRotMatrix(double angleDeg, char axis) {
    double angleRad = angleDeg * M_PI / 180;
    Eigen::Matrix4d mat = Eigen::Matrix4d::Identity();

    if(axis == 'X') {
        mat(1, 1) = cos(angleRad);
        mat(1, 2) = -sin(angleRad);
        mat(2, 1) = sin(angleRad);
        mat(2, 2) = cos(angleRad);
    } else if(axis == 'Y') {
        mat(0, 0) = cos(angleRad);
        mat(0, 2) = sin(angleRad);
        mat(2, 0) = -sin(angleRad);
        mat(2, 2) = cos(angleRad);
    } else if(axis == 'Z') {
        mat(0, 0) = cos(angleRad);
        mat(0, 1) = -sin(angleRad);
        mat(1, 0) = sin(angleRad);
        mat(1, 1) = cos(angleRad);
    }

    return mat;
}
