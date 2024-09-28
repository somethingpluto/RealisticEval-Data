import { adjustToCMajor } from './yourFileName'; // Make sure to import your function

describe("adjustToCMajor", () => {
    test("note already in C major", () => {
        expect(adjustToCMajor("C4")).toBe("C4");
        expect(adjustToCMajor("G3")).toBe("G3");
    });

    test("note not in C major", () => {
        expect(adjustToCMajor("C#4")).toBe("D4");
        expect(adjustToCMajor("F#3")).toBe("G3");
    });

    test("invalid note name", () => {
        expect(adjustToCMajor("H2")).toBe("C4");
    });

    test("edge case near C major", () => {
        expect(adjustToCMajor("B#3")).toBe("C4");
        expect(adjustToCMajor("E#4")).toBe("F4");
    });
});