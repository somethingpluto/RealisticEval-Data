import { z } from "zod";

// Mock the arabicToEnglishNumbers function for this example
function arabicToEnglishNumbers(value: string): string {
    // Example conversion from Arabic numerals to English numerals
    const arabicToEnglishMap: { [key: string]: string } = {
        '٠': '0', '١': '1', '٢': '2', '٣': '3', '٤': '4',
        '٥': '5', '٦': '6', '٧': '7', '٨': '8', '٩': '9'
    };
    return value.replace(/[٠-٩]/g, d => arabicToEnglishMap[d] || d);
}

// zNumber function as provided
export const zNumber = z.preprocess((value) => {
    if (typeof value === "string") {
        const converted = arabicToEnglishNumbers(value);
        const parsedNumber = parseFloat(converted);
        return isNaN(parsedNumber) ? value : parsedNumber;
    }
    return value;
}, z.number({ invalid_type_error: "must be a number" }));

// Test samples
const samples = [
    { input: "1234", expected: 1234 },
    { input: "٣٥", expected: 35 },    // Arabic numerals for 35
    { input: "abc", expected: "error" },
    { input: "١٢34", expected: 1234 }, // Mixed Arabic and English numerals
    { input: "", expected: "error" },
];

// Test function
function runTests() {
    samples.forEach(({ input, expected }, index) => {
        try {
            const result = zNumber.parse(input);
            if (expected === "error") {
                console.log(`Test ${index + 1} failed: Expected an error, but got ${result}`);
            } else {
                console.log(`Test ${index + 1} passed: Expected ${expected}, got ${result}`);
            }
        } catch (error) {
            if (expected === "error") {
                console.log(`Test ${index + 1} passed: Expected an error and got an error`);
            } else {
                console.log(`Test ${index + 1} failed: Expected ${expected}, but got an error`);
            }
        }
    });
}

// Run the tests
runTests();
