/**
 * Gets the current date and returns it as YYYY-MM-DD
 *
 * @returns {string} The current date formatted as YYYY-MM-DD.
 */
function getCurrentDate() {
    const now = new Date();
    const year = now.getFullYear();
    const month = String(now.getMonth() + 1).padStart(2, '0');
    const day = String(now.getDate()).padStart(2, '0');
    return `${year}-${month}-${day}`;
}
describe('getCurrentDate', () => {
    test('should return a string in the format YYYY-MM-DD', () => {
        const date = getCurrentDate();
        expect(typeof date).toBe('string');
        expect(date).toMatch(/^\d{4}-\d{2}-\d{2}$/);
    });

    test('should return the correct date for today', () => {
        const expectedDate = new Date().toISOString().split('T')[0];
        const actualDate = getCurrentDate();
        expect(actualDate).toBe(expectedDate);
    });

    test('should return the correct year part in YYYY-MM-DD', () => {
        const currentYear = new Date().getFullYear().toString();
        const actualDate = getCurrentDate();
        expect(actualDate.startsWith(currentYear)).toBe(true);
    });

    test('should return the correct month part in YYYY-MM-DD', () => {
        const currentMonth = (`0${new Date().getMonth() + 1}`).slice(-2); // Add leading zero if needed
        const actualDate = getCurrentDate();
        expect(actualDate.slice(5, 7)).toBe(currentMonth);
    });

    test('should return the correct day part in YYYY-MM-DD', () => {
        const currentDay = (`0${new Date().getDate()}`).slice(-2); // Add leading zero if needed
        const actualDate = getCurrentDate();
        expect(actualDate.slice(8, 10)).toBe(currentDay);
    });
});
