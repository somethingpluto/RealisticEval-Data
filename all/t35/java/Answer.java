package org.real.temp;

import java.util.List;
import java.util.ArrayList;

public class Answer {

    /**
     * Determine if the point (x, y) is inside the given polygon.
     * The polygon is defined as a list of tuples (x, y) representing the vertices.
     *
     * @param point  A tuple (x, y) representing the point to check.
     * @param polygon A list of tuples (x, y) representing the vertices of the polygon.
     * @return True if the point is inside the polygon, False otherwise.
     */
    public static boolean isPointInPolygon(Point point, List<Point> polygon) {
        double x = point.x;
        double y = point.y;
        boolean inside = false;
        int n = polygon.size();
        Point p1 = polygon.get(0);

        for (int i = 0; i < n + 1; i++) {
            Point p2 = polygon.get(i % n);
            if (y > Math.min(p1.y, p2.y)) {
                if (y <= Math.max(p1.y, p2.y)) {
                    if (x <= Math.max(p1.x, p2.x)) {
                        if (p1.y != p2.y) {
                            double xinters = (y - p1.y) * (p2.x - p1.x) / (p2.y - p1.y) + p1.x;
                            if (p1.x == p2.x || x <= xinters) {
                                inside = !inside;
                            }
                        } else if (p1.x == p2.x && x == p1.x) {
                            inside = !inside;
                        }
                    }
                }
            }
            p1 = p2;
        }

        return inside;
    }

    public static void main(String[] args) {
        // Example usage
        Point point = new Point(3, 3);
        List<Point> polygon = new ArrayList<>();
        polygon.add(new Point(0, 0));
        polygon.add(new Point(5, 0));
        polygon.add(new Point(5, 5));
        polygon.add(new Point(0, 5));

        System.out.println(isPointInPolygon(point, polygon)); // Output: true or false
    }

    static class Point {
        double x;
        double y;

        Point(double x, double y) {
            this.x = x;
            this.y = y;
        }
    }
}