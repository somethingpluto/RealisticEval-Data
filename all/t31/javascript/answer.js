/**
 * Calculate the proportion of red in a list of pixels.
 *
 * @param {Array<Array<number>>} pixels - A list of pixels, where each pixel is represented as an array [R, G, B].
 * @returns {number} The proportion of red in the list of pixels, as a value between 0 and 1.
 */
function calculateRedProportion(pixels) {

    if (!pixels.length) {
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