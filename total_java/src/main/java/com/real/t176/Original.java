package com.real.t176;

import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;

public class Original {
    // finds the k nearest neighbors of query point in list of points
    public static List<Point> findKNearestNeighbors(Point query, List<Point> points, int k) {

        // maxHeap to contain the neighbors
        PriorityQueue<Point> maxHeap = new PriorityQueue<>(
                (a, b) -> Double.compare(b.distanceTo(query), a.distanceTo(query))); // comparator used in Heap
        // * good, but this comparator means that we have
        // to compute the same distance many times…
        // may be a good idea to store each computed
        // distance value

        for (Point p : points) {
            maxHeap.offer(p);          // insert p in Heap
            // * well, it could be better to test is p will become
            // the root of the heap before we insert it… otherwise
            // we insert and remove the same point

            if (maxHeap.size() > k) {  // if Heap is full
                maxHeap.poll();        // removeMax from Heap
            }
        }
        // transfer neighbors to a list in order
        List<Point> neighbors = new ArrayList<>();
        while (!maxHeap.isEmpty()) {
            neighbors.add(maxHeap.poll());
        }
        return neighbors;
    }

    class Point {
        double[] coordinates;

        public Point(double... coordinates) {
            this.coordinates = coordinates;
        }

        public double distanceTo(Point other) {
            double sum = 0;
            for (int i = 0; i < coordinates.length; i++) {
                double diff = coordinates[i] - other.coordinates[i];
                sum += diff * diff;
            }
            return Math.sqrt(sum);
        }

        @Override
        public String toString() {
            StringBuilder sb = new StringBuilder("(");
            for (double coordinate : coordinates) {
                sb.append(coordinate).append(", ");
            }
            sb.setLength(sb.length() - 2);
            sb.append(")");
            return sb.toString();
        }
    }