package org.real.temp;
import java.util.PriorityQueue;
import java.util.Comparator;
public class Answer {
    static class Point {
        double x, y;

        public Point(double x, double y) {
            this.x = x;
            this.y = y;
        }

        public double distanceTo(Point other) {
            return Math.sqrt(Math.pow(this.x - other.x, 2) + Math.pow(this.y - other.y, 2));
        }
    }

    public Point[] findKNearestNeighbors(Point[] points, Point queryPoint, int k) {
        // Max-heap to store the k closest points
        PriorityQueue<Point> maxHeap = new PriorityQueue<>(k, Comparator.comparingDouble(p -> -p.distanceTo(queryPoint)));

        for (Point point : points) {
            if (maxHeap.size() < k) {
                maxHeap.offer(point);
            } else if (point.distanceTo(queryPoint) < maxHeap.peek().distanceTo(queryPoint)) {
                maxHeap.poll();
                maxHeap.offer(point);
            }
        }

        return maxHeap.toArray(new Point[0]);
    }
}
