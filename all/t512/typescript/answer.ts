function convertToRingFormat(holes: number[]): number[] {
    // Create an array of 32 elements initialized to 1
    const ring: number[] = new Array(32).fill(1);

    // Mark the positions of holes as 0
    for (let hole of holes) {
        if (hole >= 0 && hole < 32) {  // Ensure hole positions are within valid range
            ring[hole] = 0;
        }
    }

    return ring;
}
