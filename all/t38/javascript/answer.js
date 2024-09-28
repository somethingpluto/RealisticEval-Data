function rainbowHexGenerator(numIntermediates, includeEndpoints = false) {
    // List of main rainbow colors
    const rainbowColors = [
        "#FF0000",  // Red
        "#FF7F00",  // Orange
        "#FFFF00",  // Yellow
        "#00FF00",  // Green
        "#0000FF",  // Blue
        "#4B0082",  // Indigo
        "#8A2BE2"   // Violet
    ];

    // Generate intermediate colors between two hex colors
    function interpolateColors(color1, color2, steps) {
        const r1 = parseInt(color1.slice(1, 3), 16);
        const g1 = parseInt(color1.slice(3, 5), 16);
        const b1 = parseInt(color1.slice(5, 7), 16);

        const r2 = parseInt(color2.slice(1, 3), 16);
        const g2 = parseInt(color2.slice(3, 5), 16);
        const b2 = parseInt(color2.slice(5, 7), 16);

        const colors = [];

        for (let i = 1; i < steps; i++) {
            const r = Math.round(r1 + (i * (r2 - r1) / steps));
            const g = Math.round(g1 + (i * (g2 - g1) / steps));
            const b = Math.round(b1 + (i * (b2 - b1) / steps));
            colors.push(`#${r.toString(16).padStart(2, '0').toUpperCase()}${g.toString(16).padStart(2, '0').toUpperCase()}${b.toString(16).padStart(2, '0').toUpperCase()}`);
        }

        return colors;
    }

    // Calculate the full spectrum of colors
    const fullSpectrum = [];
    const numMainColors = rainbowColors.length;

    for (let i = 0; i < numMainColors - 1 + includeEndpoints; i++) {
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