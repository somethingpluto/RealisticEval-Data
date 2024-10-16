/**
 * Calculate the proportion of red in a list of pixels.
 *
 * @param pixels - An array of pixels, where each pixel is represented as a tuple of [R, G, B].
 * @returns The proportion of red in the list of pixels, as a value between 0 and 1.
 */
function calculateRedProportion(pixels: [number, number, number][]): number {

    if (pixels.length === 0) {
        return 0.0;
    }

    let totalRed = 0;
    let totalIntensity = 0;

    for (const [r, g, b] of pixels) {
        totalRed += r;
        totalIntensity += (r + g + b);
    }

    // Avoid division by zero
    if (totalIntensity === 0) {
        return 0.0;
    }

    const redProportion = totalRed / totalIntensity;
    return redProportion;
}