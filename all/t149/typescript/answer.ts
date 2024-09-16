export function hslToRgb(hue: number, saturation: number, lightness: number): { r: number, g: number, b: number } {
    // Normalize hue to be within [0, 360)
    hue = (hue % 360 + 360) % 360;

    // Convert saturation and lightness to the range of [0, 1]
    const s = saturation / 100;
    const l = lightness / 100;

    // Calculate chroma, secondary color, and match value
    const c = (1 - Math.abs(2 * l - 1)) * s;
    const x = c * (1 - Math.abs((hue / 60) % 2 - 1));
    const m = l - c / 2;

    // Determine RGB values based on the hue range
    const [r1, g1, b1] = (() => {
        if (hue < 60) return [c, x, 0];
        if (hue < 120) return [x, c, 0];
        if (hue < 180) return [0, c, x];
        if (hue < 240) return [0, x, c];
        if (hue < 300) return [x, 0, c];
        return [c, 0, x];
    })();

    // Convert to RGB values on the [0, 255] scale
    const r = Math.round((r1 + m) * 255);
    const g = Math.round((g1 + m) * 255);
    const b = Math.round((b1 + m) * 255);

    return { r, g, b };
}
