function floatToRGB(value) {
    /**
     * Convert a floating-point number between 0 and 1 to a color from red to green in RGB format.
     *
     * @param {number} value - A float between 0 and 1.
     * @returns {Array} An array representing the RGB color.
     */
    if (!(0.0 <= value && value <= 1.0)) {
        throw new Error("Value must be between 0 and 1 inclusive.");
    }

    // Calculate the red and green components
    const red = Math.floor((1.0 - value) * 255);
    const green = Math.floor(value * 255);

    // Blue component is always 0 for the red-to-green gradient
    const blue = 0;

    return [red, green, blue];
}