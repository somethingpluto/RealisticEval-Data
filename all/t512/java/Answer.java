package org.real.temp;

import java.util.ArrayList;
import java.util.List;

public class Answer {
    /**
     * Convert a list of hole positions to the ring format (list of 1s and 0s).
     *
     * @param holes A list of integers representing the positions of the holes (0-indexed).
     * @return A list of length 32, where positions with holes are 0 and others are 1.
     */
    public static List<Integer> convertToRingFormat(List<Integer> holes) {
        // Initialize the ring with all positions set to 1
        List<Integer> ring = new ArrayList<>();
        for (int i = 0; i < 32; i++) {
            ring.add(1);
        }

        // Mark the positions of holes as 0
        for (Integer hole : holes) {
            if (0 <= hole && hole < 32) {  // Ensure hole positions are within valid range
                ring.set(hole, 0);
            }
        }

        return ring;
    }

    public static void main(String[] args) {
        // Example usage
        List<Integer> holes = new ArrayList<>();
        holes.add(5);
        holes.add(10);
        holes.add(15);

        List<Integer> ring = convertToRingFormat(holes);
        System.out.println(ring);
    }
}