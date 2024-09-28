function rgbToHsv(r: number, g: number, b: number): [number, number, number] {
    // Normalize the RGB values by dividing by 255
    r = r / 255.0;
    g = g / 255.0;
    b = b / 255.0;
    
    // Find the minimum and maximum values among R, G, and B
    const maxRgb = Math.max(r, g, b);
    const minRgb = Math.min(r, g, b);
    const delta = maxRgb - minRgb;

    let h: number;
    let s: number;
    const v: number = maxRgb;

    // Calculate H (Hue)
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

    if (h < 0) {
        h += 360;  // Ensure hue is non-negative
    }

    // Calculate S (Saturation)
    if (maxRgb === 0) {
        s = 0;
    } else {
        s = delta / maxRgb;
    }

    return [h, s, v];
}