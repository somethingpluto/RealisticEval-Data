// ... (previous code for context)

export function getDaysInMonth(year: number, month: number): number {
  if (year < 0) {
    throw new Error('Year must be a positive integer.');
  }
  if (month < 1 || month > 12) {
    throw new Error('Month must be between 1 and 12.');
  }
  // ... (rest of the function remains unchanged)
}

// ... (rest of the code for context)
describe("getDaysInMonth function", () => {
    describe("Regular months", () => {
        test("January", () => {
            expect(getDaysInMonth(2023, 1)).toBe(31);
        });
        test("March", () => {
            expect(getDaysInMonth(2023, 3)).toBe(31);
        });
        test("April", () => {
            expect(getDaysInMonth(2023, 4)).toBe(30);
        });
        test("May", () => {
            expect(getDaysInMonth(2023, 5)).toBe(31);
        });
        test("June", () => {
            expect(getDaysInMonth(2023, 6)).toBe(30);
        });
        test("July", () => {
            expect(getDaysInMonth(2023, 7)).toBe(31);
        });
        test("August", () => {
            expect(getDaysInMonth(2023, 8)).toBe(31);
        });
        test("September", () => {
            expect(getDaysInMonth(2023, 9)).toBe(30);
        });
        test("October", () => {
            expect(getDaysInMonth(2023, 10)).toBe(31);
        });
        test("November", () => {
            expect(getDaysInMonth(2023, 11)).toBe(30);
        });
        test("December", () => {
            expect(getDaysInMonth(2023, 12)).toBe(31);
        });
    });

    describe("February in leap year", () => {
        test("Leap year", () => {
            expect(getDaysInMonth(2024, 2)).toBe(29);
        });
    });

    describe("February in non-leap year", () => {
        test("Non-leap year", () => {
            expect(getDaysInMonth(2023, 2)).toBe(28);
        });
    });
});
