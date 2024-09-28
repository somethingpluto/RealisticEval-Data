import { stringSideBySide } from './yourModule';  // Adjust the import according to your module's location

describe("stringSideBySide", () => {

    it("should handle strings of equal length", () => {
        const str1 = "Hello\nWorld";
        const str2 = "Python\nCode";
        const result = stringSideBySide(str1, str2);
        const expected = "Hello                | Python              \nWorld                | Code                ";
        expect(result).toEqual(expected);
    });

    it("should handle the first string being longer", () => {
        const str1 = "Hello\nWorld\nTest";
        const str2 = "Python\nCode";
        const result = stringSideBySide(str1, str2);
        const expected = "Hello                | Python              \nWorld                | Code                \nTest                 |                     ";
        expect(result).toEqual(expected);
    });

    it("should handle the second string being longer", () => {
        const str1 = "Hello\nWorld";
        const str2 = "Python\nCode\nTest";
        const result = stringSideBySide(str1, str2);
        const expected = "Hello                | Python              \nWorld                | Code                \n                     | Test                ";
        expect(result).toEqual(expected);
    });

    it("should handle an empty first string", () => {
        const str1 = "";
        const str2 = "Python\nCode";
        const result = stringSideBySide(str1, str2);
        const expected = "                     | Python              \n                     | Code                ";
        expect(result).toEqual(expected);
    });

    it("should handle custom column width", () => {
        const str1 = "Hello\nWorld";
        const str2 = "Python\nCode";
        const result = stringSideBySide(str1, str2, 10);
        const expected = "Hello      | Python    \nWorld      | Code      ";
        expect(result).toEqual(expected);
    });

});