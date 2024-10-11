describe('getMinSeqNumAndDistance', () => {
  it('should return the correct min seq num and distance', async () => {
    const filePath = 'path_to_your_file.txt'; // replace with your file path
    const word1 = 'word1';
    const word2 = 'word2';

    const result = await getMinSeqNumAndDistance(filePath, word1, word2);

    expect(result).toEqual([expectedLineNumber, expectedMinDistance]); // replace with the expected values
  });

  it('should return (null, Infinity) when one of the words is not found', async () => {
    const filePath = 'path_to_your_file.txt'; // replace with your file path
    const word1 = 'word1';
    const word2 = 'non_existent_word';

    const result = await getMinSeqNumAndDistance(filePath, word1, word2);

    expect(result).toEqual([null, Infinity]);
  });
});