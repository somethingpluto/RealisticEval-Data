/**
 * @brief Changes the reference frame of a point cloud based on three reference points.
 *
 * This function takes a point cloud and a set of three points that define a new reference frame.
 * It calculates a rotation matrix and a translation vector to transform the point cloud into 
 * the new reference frame, which is defined by the three input points.
 *
 * @param pointCloud A MatrixXd representing a collection of 3D points (Nx3), where each row 
 *                   corresponds to a point in the format [x, y, z].
 * @param refFramePoints A vector of Vector3d containing three points (A, B, C) in 3D space 
 *                       that define the new reference frame. These points should not be collinear.
 *
 * @return A MatrixXd representing the transformed point cloud in the new reference frame.
 */
 MatrixXd changeReferenceFrame(const MatrixXd &pointCloud, const vector<Vector3d> &refFramePoints) {}