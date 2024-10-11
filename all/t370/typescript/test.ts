describe('decompose function', () => {
  it('should correctly decompose a flat index into a multidimensional index', () => {
    expect(decompose(5, [3, 2])).toEqual([1, 1]);
    expect(decompose(0, [2, 3])).toEqual([0, 0]);
    expect(decompose(8, [2, 4])).toEqual([2, 0]);
  });

  it('should throw an error if the flat index is out of bounds', () => {
    expect(() => decompose(9, [2, 4])).toThrowError('Flat index out of bounds');
    expect(() => decompose(-1, [2, 4])).toThrowError('Flat index out of bounds');
  });
});