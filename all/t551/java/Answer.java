package org.real.temp;

import java.util.Arrays;

public class Answer {

    /**
     * Calculate the midpoints from a given array of edges.
     *
     * @param edges An array of edge values.
     * @return An array of midpoints calculated from the edges.
     */
    public static double[] getMidsFromEdges(double[] edges) {
        // Ensure edges is not null
        if (edges == null || edges.length < 2) {
            throw new IllegalArgumentException("Edges array must have at least two elements.");
        }

        // Calculate midpoints
        double[] mids = new double[edges.length - 1];
        for (int i = 0; i < edges.length - 1; i++) {
            mids[i] = (edges[i] + edges[i + 1]) / 2;
        }

        return mids;
    }

    public static void main(String[] args) {
        double[] edges = {1.0, 3.0, 5.0, 7.0};
        double[] mids = getMidsFromEdges(edges);
        System.out.println(Arrays.toString(mids));
    }
}