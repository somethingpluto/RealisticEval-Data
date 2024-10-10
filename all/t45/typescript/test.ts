describe('get_current_date_info', () => {
    it('should return correct date info for a given date', () => {
        const testDate = new Date(2024, 1, 29); // February 29, 2024
        const result = get_current_date_info(testDate);
        expect(result).toEqual({
            'year': 2024,
            'month': 'February',
            'week_of_the_month': 5,
            'day_of_the_week': 'Wednesday'
        });
    });

    it('should return correct date info for today\'s date', () => {
        const today = new Date();
        const result = get_current_date_info(today);
        expect(result.year).toBe(today.getFullYear());
        expect(result.month).toBe(today.toLocaleString('default', { month: 'long' }));
        expect(result.week_of_the_month).toBe(Math.ceil(today.getDate() / 7));
        expect(result.day_of_the_week).toBe(today.toLocaleString('default', { weekday: 'long' }));
    });
});