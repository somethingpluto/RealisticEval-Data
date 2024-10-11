describe('UniqueDeque', () => {
    let uniqueDeque;
  
    beforeEach(() => {
      uniqueDeque = new UniqueDeque();
    });
  
    describe('add method', () => {
      test('adds an item when it is not present', () => {
        expect(uniqueDeque.add(1)).toBe(true);
        expect(uniqueDeque.add(2)).toBe(true);
      });
  
      test('does not add an item when it is already present', () => {
        uniqueDeque.add(1);
        expect(uniqueDeque.add(1)).toBe(false);
      });
    });
  
    // Similarly, implement tests for other methods...
  });