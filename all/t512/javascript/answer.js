function convertToRingFormat(holes) {
    let ring = new Array(32).fill(1);

    // Mark the positions of holes as 0
    for (let hole of holes) {
        if (0 <= hole && hole < 32) {  // Ensure hole positions are within valid range
            ring[hole] = 0;
        }
    }

    return ring;
}