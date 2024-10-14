#include <Eigen/Dense>
#include <cmath>

double get_rotation(Eigen::Matrix2d matrix) {
    double cos_angle = (matrix(0,0) + matrix(1,1)) / 2;
    if (cos_angle > 1)
        cos_angle = 1; // Avoid acos domain error
    else if (cos_angle < -1)
        cos_angle = -1; // Avoid acos domain error

    double angle = std::acos(cos_angle);

    if ((matrix(0,1) - matrix(1,0)) < 0)
        angle = -angle;

    return angle;
}