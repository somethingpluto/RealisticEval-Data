describe('getCurrentDate', () => {
    test('should return a string in the format YYYY-MM-DD', () => {
        const date: string = getCurrentDate();
        expect(typeof date).toBe('string');
        expect(date).toMatch(/^\d{4}-\d{2}-\d{2}$/);
    });

    test('should return the correct date for today', () => {
        const expectedDate: string = new Date().toISOString().split('T')[0];
        const actualDate: string = getCurrentDate();
        expect(actualDate).toBe(expectedDate);
    });

    test('should return the correct year part in YYYY-MM-DD', () => {
        const currentYear: string = new Date().getFullYear().toString();
        const actualDate: string = getCurrentDate();
        expect(actualDate.startsWith(currentYear)).toBe(true);
    });

    test('should return the correct month part in YYYY-MM-DD', () => {
        const currentMonth: string = (`0${new Date().getMonth() + 1}`).slice(-2); // Add leading zero if needed
        const actualDate: string = getCurrentDate();
        expect(actualDate.slice(5, 7)).toBe(currentMonth);
    });

    test('should return the correct day part in YYYY-MM-DD', () => {
        const currentDay: string = (`0${new Date().getDate()}`).slice(-2); // Add leading zero if needed
        const actualDate: string = getCurrentDate();
        expect(actualDate.slice(8, 10)).toBe(currentDay);
    });
});