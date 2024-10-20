describe('appendOrSkipRow', () => {
  it('should append a new row if there isn\'t a row with matching values in the first three columns', async () => {
    // Mock the necessary dependencies
    const mockFileHandler = {
      writeFileSync: jest.fn(),
      openSync: jest.fn(),
      closeSync: jest.fn()
    };
    const mockReader = {
      readFileSync: jest.fn().mockReturnValue('col1,col2,col3,value\n')
    };

    // Call the function with the mocks
    await appendOrSkipRow(mockFileHandler, mockReader, ['col1', 'col2', 'col4', 'value']);

    // Expect that the function writes the new row to the file
    expect(mockFileHandler.writeFileSync).toHaveBeenCalledWith(expect.stringContaining('col1,col2,col4,value'));
  });

  it('should skip appending a new row if there is a row with matching values in the first three columns', async () => {
    // Mock the necessary dependencies
    const mockFileHandler = {
      writeFileSync: jest.fn(),
      openSync: jest.fn(),
      closeSync: jest.fn()
    };
    const mockReader = {
      readFileSync: jest.fn().mockReturnValue('col1,col2,col3,value\n')
    };

    // Call the function with the mocks
    await appendOrSkipRow(mockFileHandler, mockReader, ['col1', 'col2', 'col3', 'value']);

    // Expect that the function does not write the new row to the file
    expect(mockFileHandler.writeFileSync).not.toHaveBeenCalled();
  });
});