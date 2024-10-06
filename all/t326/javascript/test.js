describe('calculateTimeDifference', () => {
    test('should return correct time difference for a date in the past', () => {
        const pastDate = new Date(Date.now() - 3 * 24 * 60 * 60 * 1000 - 5 * 60 * 1000); // 3 days and 5 minutes ago
        const result = calculateTimeDifference(pastDate);
        expect(result).toEqual({ days: 3, hours: 0, minutes: 5 });
    });

    test('should return correct time difference for a date that is exactly now', () => {
        const now = new Date();
        const result = calculateTimeDifference(now);
        expect(result).toEqual({ days: 0, hours: 0, minutes: 0 });
    });

    test('should return correct time difference for a date just seconds ago', () => {
        const justNow = new Date(Date.now() - 45 * 1000); // 45 seconds ago
        const result = calculateTimeDifference(justNow);
        expect(result).toEqual({ days: 0, hours: 0, minutes: 0 });
    });


    test('should return correct time difference for a date with only hours difference', () => {
        const hoursAgo = new Date(Date.now() - 7 * 60 * 60 * 1000); // 7 hours ago
        const result = calculateTimeDifference(hoursAgo);
        expect(result).toEqual({ days: 0, hours: 7, minutes: 0 });
    });

    test('should return correct time difference for a date with hours and minutes difference', () => {
        const hoursAndMinutesAgo = new Date(Date.now() - (1 * 24 * 60 * 60 * 1000 + 3 * 60 * 1000)); // 1 day and 3 minutes ago
        const result = calculateTimeDifference(hoursAndMinutesAgo);
        expect(result).toEqual({ days: 1, hours: 0, minutes: 3 });
    });

});
