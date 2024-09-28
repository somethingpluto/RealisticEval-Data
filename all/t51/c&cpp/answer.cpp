#include <iostream>
#include <vector>
#include <Eigen/Dense>

using namespace std;
using namespace Eigen;

MatrixXd changeReferenceFrame(const MatrixXd &pointCloud, const vector<Vector3d> &refFramePoints) {
    // Unpack the three points defining the new reference frame
    Vector3d A = refFramePoints[0];
    Vector3d B = refFramePoints[1];
    Vector3d C = refFramePoints[2];

    // Compute the new basis vectors
    Vector3d u = B - A;  // Vector from A to B
    Vector3d w = u.cross(C - A);  // Orthogonal vector to the plane defined by A, B, and C
    Vector3d v = w.cross(u);  // Vector orthogonal to both u and w

    // Normalize the basis vectors to form an orthonormal basis
    u.normalize();
    v.normalize();
    w.normalize();

    // Construct the rotation matrix from the old basis to the new basis
    Matrix3d rotationMatrix;
    rotationMatrix.col(0) = u;
    rotationMatrix.col(1) = v;
    rotationMatrix.col(2) = w;

    // Calculate the translation vector to shift origin to A
    Vector3d translationVector = -rotationMatrix * A;

    // Apply the rotation and translation to the point cloud
    MatrixXd transformedPointCloud = (pointCloud.rowwise() - A.transpose()) * rotationMatrix + translationVector.transpose();

    return transformedPointCloud;
}

int main() {
    // Example usage of the changeReferenceFrame function

    // Define the original point cloud (Nx3)
    MatrixXd pointCloud(3, 3);
    pointCloud << 1.0, 2.0, 3.0,
                  4.0, 5.0, 6.0,
                  7.0, 8.0, 9.0;

    // Define the three points that define the new reference frame
    vector<Vector3d> refFramePoints = {
        Vector3d(1.0, 0.0, 0.0),
        Vector3d(0.0, 1.0, 0.0),
        Vector3d(0.0, 0.0, 1.0)
    };

    // Change the reference frame
    MatrixXd transformedPointCloud = changeReferenceFrame(pointCloud, refFramePoints);

    // Print the transformed point cloud
    cout << "Transformed Point Cloud:\n" << transformedPointCloud << endl;

    return 0;
}