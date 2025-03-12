import { sanitize } from 'some-sanitization-library'; // Replace with actual library

function wordFilterCounter(text: string, filterWords: string[]): Record<string, number> {
  const sanitizedText = sanitize(text);
  const wordCounts: Record<string, number> = {};

  filterWords.forEach(word => {
    const regex = new RegExp(`\\b${sanitize(word)}\\b`, 'gi');
    const count = (sanitizedText.match(regex) || []).length;
    wordCounts[word] = count;
  });

  return wordCounts;
}
describe('TestWordFilterCounter', () => {
  it('should correctly count words in case 1', () => {
    const text = "go to the school. go to the park.";
    const filterWords = ["go", "to", "the", "school", "park", "play"];
    const expectedOutput: Record<string, number> = {
      "go": 2,
      "to": 2,
      "the": 2,
      "school": 1,
      "park": 1,
      "play": 0
    };
    expect(wordFilterCounter(text, filterWords)).toEqual(expectedOutput);
  });

  it('should correctly count words in case 2', () => {
    const text = "This is a completely different sentence.";
    const filterWords = ["I'll", "go", "to", "the", "school", "park", "play"];
    const expectedOutput: Record<string, number> = {
      "I'll": 0,
      "go": 0,
      "to": 0,
      "the": 0,
      "school": 0,
      "park": 0,
      "play": 0
    };
    expect(wordFilterCounter(text, filterWords)).toEqual(expectedOutput);
  });

  it('should correctly count words in case 3', () => {
    const text = "I will not go to the school's park.";
    const filterWords = ["I", "will", "not", "go", "to", "the", "school's", "park"];
    const expectedOutput: Record<string, number> = {
      "I": 1,
      "will": 1,
      "not": 1,
      "go": 1,
      "to": 1,
      "the": 1,
      "school's": 1,
      "park": 1,
    };
    expect(wordFilterCounter(text, filterWords)).toEqual(expectedOutput);
  });
});
