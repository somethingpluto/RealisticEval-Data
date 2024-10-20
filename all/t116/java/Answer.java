package org.real.temp;

public class Answer {
    public static double[] toroidalDiff(Point thisPoint, Point otherPoint, double width, double height) {
        double dx = thisPoint.x - otherPoint.x;
        double dy = thisPoint.y - otherPoint.y;

        // Handle wraparound for the x dimension
        if (Math.abs(dx) > width / 2) {
            dx = dx > 0 ? dx - width : dx + width;
        }

        // Handle wraparound for the y dimension
        if (Math.abs(dy) > height / 2) {
            dy = dy > 0 ? dy - height : dy + height;
        }

        return new double[]{dx, dy};
    }

    public static class Point {
        public double x;
        public double y;

        public Point(double x, double y) {
            this.x = x;
            this.y = y;
        }
    }
}