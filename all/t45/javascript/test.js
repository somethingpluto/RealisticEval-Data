describe('get_current_date_info', () => {
    it('should return the correct date information for a given date', () => {
      const testDate = new Date(2024, 1, 29); // February 29, 2024
      const result = get_current_date_info(testDate);
  
      expect(result).toEqual({
        year: 2024,
        month: 'February',
        week_of_the_month: 5,
        day_of_the_week: 'Thursday'
      });
    });
  
    it('should return the correct date information for today\'s date if no date is provided', () => {
      const today = new Date();
      const result = get_current_date_info();
  
      expect(result.year).toBe(today.getFullYear());
      expect(result.month).toBe(today.toLocaleString('default', { month: 'long' }));
      expect(result.day_of_the_week).toBe(today.toLocaleString('default', { weekday: 'long' }));
    });
  });