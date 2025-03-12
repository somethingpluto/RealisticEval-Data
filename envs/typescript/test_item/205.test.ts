import { format } from 'date-fns';

/**
 * Retrieves the current system date and formats it as a string in the format "YYYY-MM-DD".
 *
 * @return A string representing the current date in the format "YYYY-MM-DD".
 */
function getCurrentDate(): string {
    return format(new Date(), 'yyyy-MM-dd');
}
describe("getCurrentDate function", () => {
    test("Correct format YYYY-MM-DD", () => {
        const currentDate = getCurrentDate();
        expect(currentDate.length).toBe(10);
        expect(currentDate[4]).toBe('-');
        expect(currentDate[7]).toBe('-');
    });

    test("Returns correct year", () => {
        const now = new Date();
        const currentYear = now.getFullYear();

        const currentDate = getCurrentDate();
        const yearPart = currentDate.substr(0, 4);

        expect(parseInt(yearPart, 10)).toBe(currentYear);
    });

    test("Returns correct month", () => {
        const now = new Date();
        const currentMonth = now.getMonth() + 1; // Months are 0-indexed

        const currentDate = getCurrentDate();
        const monthPart = currentDate.substr(5, 2);

        expect(parseInt(monthPart, 10)).toBe(currentMonth);
    });

    test("Returns correct day", () => {
        const now = new Date();
        const currentDay = now.getDate();

        const currentDate = getCurrentDate();
        const dayPart = currentDate.substr(8, 2);

        expect(parseInt(dayPart, 10)).toBe(currentDay);
    });

    test("Consistency of output within the same second", () => {
        const firstCall = getCurrentDate();
        const secondCall = getCurrentDate();
        expect(firstCall).toBe(secondCall);
    });
});
