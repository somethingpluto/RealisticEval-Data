describe('TestCalculateTotalSeconds', () => {
  describe('test_complete_time', () => {
      it('should correctly calculate total seconds with full values', () => {
          const time = [1, 2, 3, 4];  // 1 day, 2 hours, 3 minutes, 4 seconds
          const expected = 93784;
          const result = calculateTotalSeconds(time);
          expect(result).toBe(expected);
      });
  });

  describe('test_partial_time', () => {
      it('should correctly calculate total seconds with partial values', () => {
          const time = [0, 2, 3];  // 0 days, 2 hours, 3 minutes
          const expected = 7380;
          const result = calculateTotalSeconds(time);
          expect(result).toBe(expected);
      });
  });

  describe('test_seconds_only', () => {
      it('should correctly calculate total seconds with only seconds provided', () => {
          const time = [7200];  // 7200 seconds
          const expected = 7200;
          const result = calculateTotalSeconds(time);
          expect(result).toBe(expected);
      });
  });

  describe('test_no_time', () => {
      it('should correctly calculate total seconds with no time values provided', () => {
          const time = [];
          const expected = 0;
          const result = calculateTotalSeconds(time);
          expect(result).toBe(expected);
      });
  });
});