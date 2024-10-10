describe('removeComments', () => {
  it('should remove comments starting with "#" and ending at the newline', () => {
    const input = "Hello, world! # This is a comment";
    const expectedOutput = "Hello, world!";
    expect(removeComments(input)).toBe(expectedOutput);
  });

  it('should handle multiple lines with comments', () => {
    const input = `
      Line1 # Comment1
      Line2 # Comment2
      Line3 # Comment3
    `;
    const expectedOutput = `
      Line1 
      Line2 
      Line3 
    `;
    expect(removeComments(input)).toBe(expectedOutput);
  });

  it('should not remove non-comment text', () => {
    const input = "Hello, world! This is not a comment.";
    const expectedOutput = "Hello, world! This is not a comment.";
    expect(removeComments(input)).toBe(expectedOutput);
  });
});