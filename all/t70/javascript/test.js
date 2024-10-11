describe('codeBlockRemover', () => {
  it('should return an empty array when there are no code blocks in the input', () => {
    const markdownString = 'This is a sample text without any code blocks.';
    expect(codeBlockRemover(markdownString)).toEqual([]);
  });

  it('should return an array with one element when there is one code block in the input', () => {
    const markdownString = 'This is a sample text with a `code block` inside.';
    expect(codeBlockRemover(markdownString)).toEqual(['code block']);
  });

  it('should return an array with multiple elements when there are multiple code blocks in the input', () => {
    const markdownString = 'This is a sample text with a `first code block`, and another `second code block` inside.';
    expect(codeBlockRemover(markdownString)).toEqual(['first code block', 'second code block']);
  });
});
