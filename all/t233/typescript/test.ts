describe('removeComments', () => {

  test('single line comment', () => {
      const inputString = "Hello, world!# This is a comment";
      const expectedOutput = "Hello, world!";
      expect(removeComments(inputString)).toBe(expectedOutput);
  });

  test('no comments', () => {
      const inputString = "Hello, world!\nPython is fun!";
      const expectedOutput = "Hello, world!\nPython is fun!";
      expect(removeComments(inputString)).toBe(expectedOutput);
  });

  test('empty string', () => {
      const inputString = "";
      const expectedOutput = "";
      expect(removeComments(inputString)).toBe(expectedOutput);
  });

  test('comments only', () => {
      const inputString = "# comment only line\n#another comment line";
      const expectedOutput = ""; // No actual content, should return an empty string
      expect(removeComments(inputString)).toBe(expectedOutput);
  });

});
