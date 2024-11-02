function rgbToHsv(r: number, g: number, b: number): [number, number, number] {
    const normalizedR = r / 255.0;
    const normalizedG = g / 255.0;
    const normalizedB = b / 255.0;
    const maxRgb = Math.max(normalizedR, normalizedG, normalizedB);
    const minRgb = Math.min(normalizedR, normalizedG, normalizedB);
    const delta = maxRgb - minRgb;
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
    h *= 60;  
    let s: number;
    if (maxRgb === 0) {
        s = 0;
    } else {
        s = delta / maxRgb;
    }
    const v = maxRgb;
    return [h, s * 100, v * 100];
}