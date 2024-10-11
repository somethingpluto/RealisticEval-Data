describe('decompose', () => {
  it('should return correct multidimensional index for valid input', () => {
    expect(decompose(5, [2, 3])).toEqual([1, 2]);
  });

  it('should throw an error if n is out of bounds', () => {
    expect(() => decompose(7, [2, 3])).toThrow('n is out of bounds');
  });
});