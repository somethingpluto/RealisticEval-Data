package org.real.temp;

import java.util.ArrayList;
import java.util.List;

public class Answer {

    /**
     * Generates integer coordinates on the line from (x1, y1) to (x2, y2) using Bresenham's line algorithm.
     * 
     * @param x1 The x-coordinate of the start point.
     * @param y1 The y-coordinate of the start point.
     * @param x2 The x-coordinate of the end point.
     * @param y2 The y-coordinate of the end point.
     * @return A list of integer coordinates representing the points on the line.
     */
    public static List<int[]> bresenhamLine(int x1, int y1, int x2, int y2) {
        List<int[]> points = new ArrayList<>();
        int dx = Math.abs(x2 - x1);
        int dy = -Math.abs(y2 - y1);
        int sx = (x1 < x2) ? 1 : -1;
        int sy = (y1 < y2) ? 1 : -1;
        int err = dx + dy; // error value e_xy

        while (true) {
            points.add(new int[]{x1, y1});
            if (x1 == x2 && y1 == y2) {
                break;
            }
            int e2 = 2 * err;
            if (e2 >= dy) { // e_xy+e_x > 0
                err += dy;
                x1 += sx;
            }
            if (e2 <= dx) { // e_xy+e_y < 0
                err += dx;
                y1 += sy;
            }
        }

        return points;
    }

    public static void main(String[] args) {
        List<int[]> points = bresenhamLine(0, 0, 5, 3);
        for (int[] point : points) {
            System.out.println("(" + point[0] + ", " + point[1] + ")");
        }
    }
}