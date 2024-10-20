describe('sanitizeData', () => {
  it('removes specified keys from the data object', () => {
    const data = {
      name: 'John Doe',
      age: 30,
      email: 'john.doe@example.com'
    };

    const result = sanitizeData(data, ['age', 'email']);
    expect(result).toEqual({ name: 'John Doe' });
  });

  it('returns the original object if no keys are provided', () => {
    const data = {
      name: 'Jane Doe',
      age: 25,
      email: 'jane.doe@example.com'
    };

    const result = sanitizeData(data);
    expect(result).toEqual(data);
  });

  it('does not modify the original object', () => {
    const data = {
      name: 'Jim Beam',
      age: 40,
      email: 'jim.beam@example.com'
    };

    const originalDataCopy = { ...data };
    sanitizeData(data, ['name']);

    expect(data).toEqual(originalDataCopy);
  });
});