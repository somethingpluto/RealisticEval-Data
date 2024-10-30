/**
 * Convert a floating-point number between 0 and 1 to a color from red to green in RGB format.
 *
 * @param value - A float between 0 and 1.
 * @returns A tuple representing the RGB color.
 */
function floatToRGB(value: number): [number, number, number] {
    if (!(0.0 <= value && value <= 1.0)) {
        throw new Error("Value must be between 0 and 1 inclusive.");
    }
    const red = Math.floor((1.0 - value) * 255);
    const green = Math.floor(value * 255);
    const blue = 0;
    return [red, green, blue];
}