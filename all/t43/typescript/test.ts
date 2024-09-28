import { rgbToHsv } from './yourModule'; // Import the rgbToHsv function from its module
import { describe, test, expect } from '@jest/globals';

describe('rgbToHsv', () => {

  test('should convert pure red color correctly', () => {
    const r = 255, g = 0, b = 0;
    const expectedResult = [0, 1, 1]; // Hue should be 0, Saturation 1, Value 1 for red
    const result = rgbToHsv(r, g, b);
    expect(result).toEqual(expectedResult);
  });

  test('should convert pure green color correctly', () => {
    const r = 0, g = 255, b = 0;
    const expectedResult = [120, 1, 1]; // Hue should be 120, Saturation 1, Value 1 for green
    const result = rgbToHsv(r, g, b);
    expect(result).toEqual(expectedResult);
  });

  test('should convert pure blue color correctly', () => {
    const r = 0, g = 0, b = 255;
    const expectedResult = [240, 1, 1]; // Hue should be 240, Saturation 1, Value 1 for blue
    const result = rgbToHsv(r, g, b);
    expect(result).toEqual(expectedResult);
  });

  test('should convert white color correctly', () => {
    const r = 255, g = 255, b = 255;
    const expectedResult = [0, 0, 1]; // Hue is undefined, typically 0; Saturation 0, Value 1 for white
    const result = rgbToHsv(r, g, b);
    expect(result).toEqual(expectedResult);
  });

  test('should convert black color correctly', () => {
    const r = 0, g = 0, b = 0;
    const expectedResult = [0, 0, 0]; // Hue is undefined, typically 0; Saturation 0, Value 0 for black
    const result = rgbToHsv(r, g, b);
    expect(result).toEqual(expectedResult);
  });

});