describe('findPlaceholders', () => {
    it('should return an empty array for an empty string', () => {
      expect(findPlaceholders('')).toEqual([]);
    });
  
    it('should return a list of placeholders for valid input', () => {
      const text = 'This is a test with {{ placeholder1 }} and {{ placeholder2 }}';
      const expectedOutput = ['placeholder1', 'placeholder2'];
      expect(findPlaceholders(text)).toEqual(expectedOutput);
    });
  
    it('should ignore non-placeholder strings', () => {
      const text = 'This is a test without any placeholders';
      expect(findPlaceholders(text)).toEqual([]);
    });
  
    it('should handle multiple placeholders correctly', () => {
      const text = '{{ placeholder1 }} {{ placeholder2 }} {{ placeholder3 }}';
      const expectedOutput = ['placeholder1', 'placeholder2', 'placeholder3'];
      expect(findPlaceholders(text)).toEqual(expectedOutput);
    });
  });