describe('appendOrSkipRow', () => {
  let fileHandler;
  let reader;

  beforeEach(() => {
    // Mocking the file handler and reader objects
    fileHandler = {
      writeFileSync: jest.fn(),
      createReadStream: jest.fn().mockReturnValue({
        pipe: jest.fn()
      })
    };

    reader = {
      on: jest.fn()
    };
  });

  it('appends a new row if there isn\'t a row with matching values in the first three columns', () => {
    const rowCandidate = ['value1', 'value2', 'value3', 'otherValue'];
    const existingRows = [
      ['value1', 'value2', 'value4'],
      ['value5', 'value6', 'value7']
    ];

    reader.on.mockImplementation((event, callback) => {
      if (event === 'data') {
        existingRows.forEach(row => {
          callback({ data: row });
        });
      }
    });

    appendOrSkipRow(fileHandler, reader, rowCandidate);

    expect(fileHandler.writeFileSync).toHaveBeenCalledWith(
      expect.any(String),
      expect.stringContaining('value1,value2,value3,otherValue')
    );
  });

  it('skips appending a new row if there is already a row with matching values in the first three columns', () => {
    const rowCandidate = ['value1', 'value2', 'value3', 'otherValue'];
    const existingRows = [
      ['value1', 'value2', 'value3'],
      ['value5', 'value6', 'value7']
    ];

    reader.on.mockImplementation((event, callback) => {
      if (event === 'data') {
        existingRows.forEach(row => {
          callback({ data: row });
        });
      }
    });

    appendOrSkipRow(fileHandler, reader, rowCandidate);

    expect(fileHandler.writeFileSync).not.toHaveBeenCalled();
  });
});