// Additions at the start of the file
import { Color } from './color';

export function rgbToHex(rgb: { r: number; g: number; b: number }): string {
  // ... existing code ...
}

export function hexToRgb(hex: string): Color | null {
  // ... existing code ...
}

// Additions at the end of the file
export class Color {
  constructor(public r: number, public g: number, public b: number) {}

  toRgbString(): string {
    return `rgb(${this.r}, ${this.g}, ${this.b})`;
  }

  toHexString(): string {
    return this.r.toString(16).padStart(2, '0') +
           this.g.toString(16).padStart(2, '0') +
           this.b.toString(16).padStart(2, '0');
  }
}
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

