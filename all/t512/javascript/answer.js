function convertToRingFormat(holes) {
    /**
     * Convert an array of hole positions to the ring format (array of 1s and 0s).
     *
     * Parameters:
     * holes (Array): An array of integers representing the positions of the holes (0-indexed).
     *
     * Returns:
     * Array: An array of length 32, where positions with holes are 0 and others are 1.
     */
    // Initialize the ring with all positions set to 1
    let ring = new Array(32).fill(1);

    // Mark the positions of holes as 0
    for (let hole of holes) {
        if (0 <= hole && hole < 32) {  // Ensure hole positions are within valid range
            ring[hole] = 0;
        }
    }

    return ring;
}