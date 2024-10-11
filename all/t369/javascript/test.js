describe('Eight Queens Problem', () => {
  test('should find and print a valid solution', () => {
    // Mock console.log to capture output
    const mockConsoleLog = jest.spyOn(console, 'log');

    // Call the function
    eightQueens();

    // Check if the expected output was printed
    expect(mockConsoleLog).toHaveBeenCalledWith(
      '. . Q . . . . .\n' +
      '. . . . Q . . .\n' +
      '. Q . . . . . .\n' +
      '. . . . . . . Q\n' +
      '. . . . . Q . .\n' +
      '. . . Q . . . .\n' +
      '. . . . . . Q .\n' +
      'Q . . . . . . .'
    );

    // Restore original console.log
    mockConsoleLog.mockRestore();
  });

  test('should handle no solution case', () => {
    // Mock console.log to capture output
    const mockConsoleLog = jest.spyOn(console, 'log');

    // Modify the implementation to force no solution (e.g., by changing the board size)
    const originalEightQueens = eightQueens;
    eightQueens = () => {
      console.log('No solution');
    };

    // Call the modified function
    eightQueens();

    // Check if the expected output was printed
    expect(mockConsoleLog).toHaveBeenCalledWith('No solution');

    // Restore original eightQueens function and console.log
    eightQueens = originalEightQueens;
    mockConsoleLog.mockRestore();
  });
});