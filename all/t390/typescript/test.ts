describe('TestSplitIntoSentences', () => {
  it('test_basic_splitting', () => {
    // Test splitting a basic text with clear punctuation
    const text = "Hello world! How are you? I am fine.";
    const expected = ["Hello world!", "How are you?", "I am fine."];
    const result = splitIntoSentences(text);
    expect(result).toEqual(expected);
  });

  it('test_complex_punctuation', () => {
    // Test splitting text that includes quotes and commas
    const text = 'He said, This is amazing! Then he left.';
    const expected = ['He said, This is amazing!', "Then he left."];
    const result = splitIntoSentences(text);
    expect(result).toEqual(expected);
  });

  it('test_with_no_punctuation', () => {
    // Test text that has no punctuation marks
    const text = "Hello world how are you";
    const expected = ["Hello world how are you"];
    const result = splitIntoSentences(text);
    expect(result).toEqual(expected);
  });

  it('test_empty_string', () => {
    // Test empty string input
    const text = "";
    const expected = [];
    const result = splitIntoSentences(text);
    expect(result).toEqual(expected);
  });
});