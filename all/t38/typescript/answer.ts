function rainbowHexGenerator(numIntermediates: number, includeEndpoints: boolean = false): string[] {
    // List of main rainbow colors
    const rainbowColors: string[] = [
        "#FF0000",  // Red
        "#FF7F00",  // Orange
        "#FFFF00",  // Yellow
        "#00FF00",  // Green
        "#0000FF",  // Blue
        "#4B0082",  // Indigo
        "#8A2BE2"   // Violet
    ];

    // Generate intermediate colors between two hex colors
    function interpolateColors(color1: string, color2: string, steps: number): string[] {
        const r1 = parseInt(color1.substring(1, 3), 16);
        const g1 = parseInt(color1.substring(3, 5), 16);
        const b1 = parseInt(color1.substring(5, 7), 16);

        const r2 = parseInt(color2.substring(1, 3), 16);
        const g2 = parseInt(color2.substring(3, 5), 16);
        const b2 = parseInt(color2.substring(5, 7), 16);

        const interpolatedColors: string[] = [];
        for (let i = 1; i < steps; i++) {
            const r = Math.round(r1 + (i * (r2 - r1) / steps));
            const g = Math.round(g1 + (i * (g2 - g1) / steps));
            const b = Math.round(b1 + (i * (b2 - b1) / steps));
            interpolatedColors.push(`#${r.toString(16).padStart(2, '0').toUpperCase()}${g.toString(16).padStart(2, '0').toUpperCase()}${b.toString(16).padStart(2, '0').toUpperCase()}`);
        }
        return interpolatedColors;
    }

    // Calculate the full spectrum of colors
    const fullSpectrum: string[] = [];
    const numMainColors = rainbowColors.length;
    for (let i = 0; i < numMainColors - 1 + (includeEndpoints ? 1 : 0); i++) {
        // Wrap around for the endpoint inclusion
        const nextIndex = (i + 1) % numMainColors;
        const currentColor = rainbowColors[i];
        const nextColor = rainbowColors[nextIndex];
        fullSpectrum.push(currentColor);
        fullSpectrum.push(...interpolateColors(currentColor, nextColor, numIntermediates + 1));
    }

    // Append the last color only if endpoints are not included
    if (!includeEndpoints) {
        fullSpectrum.push(rainbowColors[rainbowColors.length - 1]);
    }

    return fullSpectrum;
}