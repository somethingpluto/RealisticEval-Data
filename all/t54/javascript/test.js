describe('removeTripleBackticks', () => {
  it('should remove triple backticks from a string', () => {
    expect(removeTripleBackticks(['abc````def'])).toEqual(['abc``def']);
  });

  it('should remove multiple triple backticks from a string', () => {
    expect(removeTripleBackticks(['abc````def````ghi'])).toEqual(['abc``def``ghi']);
  });

  // Add more tests as needed...
});