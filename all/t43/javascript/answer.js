function rgbToHsv(r, g, b) {
    // Normalize the RGB values by dividing by 255
    r = r / 255.0;
    g = g / 255.0;
    b = b / 255.0;

    // Find the minimum and maximum values among R, G, and B
    let maxRgb = Math.max(r, g, b);
    let minRgb = Math.min(r, g, b);
    let delta = maxRgb - minRgb;

    // Calculate H (Hue)
    let h;
    if (delta === 0) {
        h = 0;
    } else if (maxRgb === r) {
        h = ((g - b) / delta) % 6;
    } else if (maxRgb === g) {
        h = ((b - r) / delta) + 2;
    } else {
        h = ((r - g) / delta) + 4;
    }

    h *= 60; // Convert to degrees on the color circle

    // Calculate S (Saturation)
    let s;
    if (maxRgb === 0) {
        s = 0;
    } else {
        s = delta / maxRgb;
    }

    // V (Value) is equal to maxRgb
    let v = maxRgb;

    return [h, s, v];
}