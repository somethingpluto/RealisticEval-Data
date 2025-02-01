/**
 * Retrieves the current system date and formats it as a string in the format "YYYY-MM-DD".
 *
 * @return {string} A string representing the current date in the format "YYYY-MM-DD".
 */
function getCurrentDate() {
    const today = new Date();
    const year = today.getFullYear();
    const month = String(today.getMonth() + 1).padStart(2, '0');
    const day = String(today.getDate()).padStart(2, '0');
    return `${year}-${month}-${day}`;
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
        const yearPart = currentDate.substring(0, 4);

        expect(Number(yearPart)).toBe(currentYear);
    });

    test("Returns correct month", () => {
        const now = new Date();
        const currentMonth = now.getMonth() + 1; // Months are 0-based in JavaScript

        const currentDate = getCurrentDate();
        const monthPart = currentDate.substring(5, 7);

        expect(Number(monthPart)).toBe(currentMonth);
    });

    test("Returns correct day", () => {
        const now = new Date();
        const currentDay = now.getDate();

        const currentDate = getCurrentDate();
        const dayPart = currentDate.substring(8, 10);

        expect(Number(dayPart)).toBe(currentDay);
    });

    test("Consistency of output within the same second", () => {
        const firstCall = getCurrentDate();
        const secondCall = getCurrentDate();
        expect(firstCall).toBe(secondCall);
    });

});
