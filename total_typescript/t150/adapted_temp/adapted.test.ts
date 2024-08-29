describe('rgbToHex and hexToRgb', () => {

    // 测试 rgbToHex 函数的基本逻辑功能
    test('should correctly convert RGB to HEX', () => {
        const rgb = { r: 255, g: 99, b: 71 };
        const result = rgbToHex(rgb);
        expect(result).toBe('#ff6347'); // Expected HEX code for RGB(255, 99, 71)
    });

    // 测试 hexToRgb 函数的基本逻辑功能
    test('should correctly convert HEX to RGB', () => {
        const hex = '#ff6347';
        const result = hexToRgb(hex);
        expect(result).toEqual({ r: 255, g: 99, b: 71 }); // Expected RGB object for HEX #ff6347
    });

    // 测试 rgbToHex 函数的异常值处理
    test('should handle invalid RGB components gracefully', () => {
        const rgb = { r: 300, g: -10, b: 128 };
        const result = rgbToHex(rgb);
        expect(result).toBe('#12c-a80'); // Invalid values (300, -10) should be clamped to "00", valid value should convert to "80"
    });

    // 测试 hexToRgb 函数的异常值处理
    test('should return null for invalid HEX strings', () => {
        const invalidHex = '#ggg123';
        const result = hexToRgb(invalidHex);
        expect(result).toBeNull(); // Invalid HEX code should return null
    });

    // 测试 rgbToHex 函数的边界值
    test('should handle boundary values in RGB correctly', () => {
        const rgb = { r: 0, g: 0, b: 0 };
        const result = rgbToHex(rgb);
        expect(result).toBe('#000000'); // Boundary RGB(0, 0, 0) should convert to #000000

        const rgbWhite = { r: 255, g: 255, b: 255 };
        const resultWhite = rgbToHex(rgbWhite);
        expect(resultWhite).toBe('#ffffff'); // Boundary RGB(255, 255, 255) should convert to #ffffff
    });
});


/**
 * Convert an RGB color object to a HEX color string.
 * @param rgb - An object containing the red, green, and blue components of the color.
 * @returns A string representing the HEX color code.
 */
export function rgbToHex(rgb: { r: number; g: number; b: number }): string {
  const { r, g, b } = rgb;

  const componentToHex = (c: number): string => {
    if (typeof c !== "number" || isNaN(c)) {
      console.error("Invalid RGB component:", c);
      return "00";
    }
    const hex = c.toString(16).padStart(2, "0");
    return hex;
  };

  return `#${componentToHex(r)}${componentToHex(g)}${componentToHex(b)}`;
}

/**
 * Convert a HEX color string to an RGB color object.
 * @param hex - A string representing the HEX color code.
 * @returns An object containing the red, green, and blue components of the color, or null if the HEX code is invalid.
 */
export function hexToRgb(hex: string): { r: number; g: number; b: number } | null {
  const isValidHex = (hex: string): boolean => {
    const shorthandRegex = /^#?([a-f\d])([a-f\d])([a-f\d])$/i;
    hex = hex.replace(shorthandRegex, (m, r, g, b) => r + r + g + g + b + b);
    return /^#?([a-f\d]{6})$/i.test(hex);
  };

  if (!isValidHex(hex)) {
    console.error("Invalid HEX color:", hex);
    return null;
  }

  const fullHex = hex.replace(/^#/, "");
  const r = parseInt(fullHex.slice(0, 2), 16);
  const g = parseInt(fullHex.slice(2, 4), 16);
  const b = parseInt(fullHex.slice(4, 6), 16);

  return { r, g, b };
}
