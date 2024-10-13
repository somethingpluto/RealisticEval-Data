function rgbToHsv(r, g, b) {
    // Normalize the RGB values by dividing by 255
    r /= 255.0;
    g /= 255.0;
    b /= 255.0;

    // Find the minimum and maximum values among R, G, and B
    const maxRgb = Math.max(r, g, b);
    const minRgb = Math.min(r, g, b);
    const delta = maxRgb - minRgb;

    // Calculate H (Hue)
    let h = 0;
    if (delta === 0) {
        h = 0;
    } else if (maxRgb === r) {
        h = ((g - b) / delta) % 6;
    } else if (maxRgb === g) {
        h = ((b - r) / delta) + 2;
    } else {
        h = ((r - g) / delta) + 4;
    }

    h *= 60;  // Convert to degrees on the color circle

    // Calculate S (Saturation)
    let s = 0;
    if (maxRgb === 0) {
        s = 0;
    } else {
        s = delta / maxRgb;
    }

    // V (Value) is equal to maxRgb
    const v = maxRgb;

    return [h, s * 100, v * 100];
}