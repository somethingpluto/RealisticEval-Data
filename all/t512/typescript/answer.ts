function convertToRingFormat(holes: number[]): number[] {
    /**
     * Convert an array of hole positions to the ring format (array of 1s and 0s).
     *
     * Parameters:
     * holes (number[]): An array of numbers representing the positions of the holes (0-indexed).
     *
     * Returns:
     * number[]: An array of length 32, where positions with holes are 0 and others are 1.
     */
    // Initialize the ring with all positions set to 1
    const ring: number[] = new Array(32).fill(1);

    // Mark the positions of holes as 0
    for (const hole of holes) {
        if (0 <= hole && hole < 32) {  // Ensure hole positions are within valid range
            ring[hole] = 0;
        }
    }

    return ring;
}