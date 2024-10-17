function hexToAnsi(hexColor: string): string {
    /**
     * Convert a hexadecimal color code to an ANSI escape code.
     *
     * Parameters:
     * hexColor (string): A string representing the hexadecimal color code, e.g., '#FF5733'.
     *
     * Returns:
     * string: An ANSI escape code for the specified RGB color.
     */

    // Check if the input is a valid hex color
    if (hexColor.length !== 7 || hexColor[0] !== '#') {
        throw new Error("Invalid hex color format. Use '#RRGGBB'.");
    }

    // Extract the red, green, and blue components from the hex string
    const r = parseInt(hexColor.substring(1, 3), 16);
    const g = parseInt(hexColor.substring(3, 5), 16);
    const b = parseInt(hexColor.substring(5, 7), 16);

    // Create the ANSI escape code
    const ansiCode = `\x1b[38;2;${r};${g};${b}m`;

    return ansiCode;
}