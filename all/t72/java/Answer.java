package org.real.temp;

public class Answer {
    public static class Point3D {
        double x;
        double y;
        double z;

        public Point3D(double x, double y, double z) {
            this.x = x;
            this.y = y;
            this.z = z;
        }

        @Override
        public String toString() {
            return "Point3D{" +
                    "x=" + x +
                    ", y=" + y +
                    ", z=" + z +
                    '}';
        }
    }

    public static Point3D get3DCoordinates(double[][] K, double d, double x, double y) {
        // Extracting elements from the camera intrinsic matrix K
        double fx = K[0][0];
        double fy = K[1][1];
        double cx = K[0][2];
        double cy = K[1][2];

        // Calculating 3D world coordinates
        double X = (x - cx) * d / fx;
        double Y = (y - cy) * d / fy;
        double Z = d;

        return new Point3D(X, Y, Z);
    }

    public static void main(String[] args) {
        // Example usage
        double[][] K = {
                {500, 0, 320},
                {0, 500, 240},
                {0, 0, 1}
        };
        double d = 10; // Depth
        double x = 300; // Pixel x coordinate
        double y = 200; // Pixel y coordinate

        Point3D result = get3DCoordinates(K, d, x, y);
        System.out.println(result);
    }
}