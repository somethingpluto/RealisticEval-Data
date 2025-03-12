// At the start of your TypeScript file
export function getDaysInMonth(year: number, month: number): number {
  // ... existing function code ...
}

// At the end of your TypeScript file
describe("getDaysInMonth", () => {
    // Test case 1: Leap year February
    test("Leap year February", () => {
        expect(getDaysInMonth(2024, 2)).toBe(29); // 2024 is a leap year
    });

    // Test case 2: Non-leap year February
    test("Non-leap year February", () => {
        expect(getDaysInMonth(2023, 2)).toBe(28); // 2023 is not a leap year
    });

    // Test case 3: Months with 31 days
    test("Month with 31 days", () => {
        expect(getDaysInMonth(2023, 1)).toBe(31); // January has 31 days
        expect(getDaysInMonth(2023, 7)).toBe(31); // July has 31 days
    });

    // Test case 4: Months with 30 days
    test("Month with 30 days", () => {
        expect(getDaysInMonth(2023, 4)).toBe(30); // April has 30 days
        expect(getDaysInMonth(2023, 11)).toBe(30); // November has 30 days
    });

    // Test case 5: Invalid months
    test("Invalid month", () => {
        expect(() => getDaysInMonth(2023, 0)).toThrow(Error);  // Month less than 1
        expect(() => getDaysInMonth(2023, 13)).toThrow(Error); // Month greater than 12
    });
});
