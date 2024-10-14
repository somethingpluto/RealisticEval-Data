describe('isBreakTime Function Tests', () => {
    test('should return true when current time is exactly at the start time', () => {
        expect(isBreakTime("09:00", "10:00", "09:00")).toBe(true);
    });

    test('should return true when current time is within the break time range', () => {
        expect(isBreakTime("09:00", "10:00", "09:30")).toBe(true);
    });

    test('should return false when current time exactly exceeds the end time', () => {
        expect(isBreakTime("09:00", "10:00", "10:00")).toBe(false);
    });

    test('should return false when current time is before the break time', () => {
        expect(isBreakTime("09:00", "10:00", "08:59")).toBe(false);
    });

    test('should return false when current time is after the break time', () => {
        expect(isBreakTime("09:00", "10:00", "10:01")).toBe(false);
    });
});