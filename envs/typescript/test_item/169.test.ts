function convertToRoman(num: number): string {
    if (isNaN(num) || num < 1 || num > 3999) {
        throw new Error("Input must be an integer between 1 and 3999.");
    }

    const romanNumerals: { [key: number]: string } = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I"
    };

    let romanNumeral: string = "";

    for (let key in romanNumerals) {
        while (num >= parseInt(key, 10)) {
            romanNumeral += romanNumerals[key];
            num -= parseInt(key, 10);
        }
    }

    return romanNumeral;
}
describe('convertToRoman', () => {

    test('should return the correct Roman numeral for a typical number', () => {
        const result = convertToRoman(1987);
        expect(result).toBe('MCMLXXXVII'); // 1987 = M + CM + LXXX + VII
    });

    test('should return the correct Roman numeral for the minimum value (1)', () => {
        const result = convertToRoman(1);
        expect(result).toBe('I'); // 1 = I
    });

    test('should return the correct Roman numeral for a large number (3999)', () => {
        const result = convertToRoman(3999);
        expect(result).toBe('MMMCMXCIX'); // 3999 = MMM + CM + XC + IX
    });

    test('should return the correct Roman numeral for a number with different numeral repeats', () => {
        const result = convertToRoman(1666);
        expect(result).toBe('MDCLXVI'); // 1666 = M + D + CLX + VI
    });

    test('should return the correct Roman numeral for number with no 5s and 1s', () => {
        const result = convertToRoman(2000);
        expect(result).toBe('MM'); // 2000 = MM
    });
});
