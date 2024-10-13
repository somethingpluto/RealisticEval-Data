describe('TestGetCurrentDateInfo', () => {
    it('should return correct info for the beginning of the month', () => {
      const result = getCurrentDateInfo(DateTime.fromJSDate(new Date(2023, 0, 1)));
      const expected = {
        year: 2023,
        month: 'January',
        weekOfTheMonth: 1,
        dayOfWeek: 'Sunday'
      };
      expect(result).toEqual(expected);
    });
  
    it('should return correct info for the middle of the month', () => {
      const result = getCurrentDateInfo(DateTime.fromJSDate(new Date(2023, 0, 15)));
      const expected = {
        year: 2023,
        month: 'January',
        weekOfTheMonth: 3,
        dayOfWeek: 'Sunday'
      };
      expect(result).toEqual(expected);
    });
  
    it('should return correct info for a leap year', () => {
      const result = getCurrentDateInfo(DateTime.fromJSDate(new Date(2024, 1, 29)));
      const expected = {
        year: 2024,
        month: 'February',
        weekOfTheMonth: 5,
        dayOfWeek: 'Thursday'
      };
      expect(result).toEqual(expected);
    });
  
    it('should return correct info for the change of year', () => {
      const result = getCurrentDateInfo(DateTime.fromJSDate(new Date(2022, 11, 31)));
      const expected = {
        year: 2022,
        month: 'December',
        weekOfTheMonth: 5,
        dayOfWeek: 'Saturday'
      };
      expect(result).toEqual(expected);
    });
  });