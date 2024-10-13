function rgbToHsv(r: number, g: number, b: number): [number, number, number] {
    // Normalize the RGB values by dividing by 255
    const normalizedR = r / 255.0;
    const normalizedG = g / 255.0;
    const normalizedB = b / 255.0;

    // Find the minimum and maximum values among R, G, and B
    const maxRgb = Math.max(normalizedR, normalizedG, normalizedB);
    const minRgb = Math.min(normalizedR, normalizedG, normalizedB);
    const delta = maxRgb - minRgb;

    // Calculate H (Hue)
    let h: number;
    if (delta === 0) {
        h = 0;
    } else if (maxRgb === normalizedR) {
        h = ((normalizedG - normalizedB) / delta) % 6;
    } else if (maxRgb === normalizedG) {
        h = ((normalizedB - normalizedR) / delta) + 2;
    } else {
        h = ((normalizedR - normalizedG) / delta) + 4;
    }

    h *= 60;  // Convert to degrees on the color circle

    // Calculate S (Saturation)
    let s: number;
    if (maxRgb === 0) {
        s = 0;
    } else {
        s = delta / maxRgb;
    }

    // V (Value) is equal to maxRgb
    const v = maxRgb;

    return [h, s * 100, v * 100];
}