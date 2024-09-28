import { rainbowHexGenerator } from './rainbowHexGenerator'; // Adjust the import to where your function is located

describe('rainbowHexGenerator', () => {
    const rainbowColors = [
        "#FF0000",  // Red
        "#FF7F00",  // Orange
        "#FFFF00",  // Yellow
        "#00FF00",  // Green
        "#0000FF",  // Blue
        "#4B0082",  // Indigo
        "#8A2BE2"   // Violet
    ];

    test('no intermediates', () => {
        const result = rainbowHexGenerator(0);
        expect(result).toEqual(rainbowColors);
    });

    test('one intermediate', () => {
        const result = rainbowHexGenerator(1);
        expect(result.length).toBe(13);
    });

    test('include endpoints', () => {
        const result = rainbowHexGenerator(1, true);
        expect(result.length).toBe(14);
    });

    test('high number of intermediates', () => {
        const result = rainbowHexGenerator(10);
        expect(result.length).toBe(67);
    });
});