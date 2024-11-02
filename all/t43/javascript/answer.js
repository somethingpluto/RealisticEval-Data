function rgbToHsv(r, g, b) {
    r /= 255.0;
    g /= 255.0;
    b /= 255.0;
    const maxRgb = Math.max(r, g, b);
    const minRgb = Math.min(r, g, b);
    const delta = maxRgb - minRgb;
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
    h *= 60;
    let s = 0;
    if (maxRgb === 0) {
        s = 0;
    } else {
        s = delta / maxRgb;
    }
    const v = maxRgb;
    return [h, s * 100, v * 100];
}