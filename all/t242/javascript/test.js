describe('classifyFilesByExtension', () => {
  it('should return an empty object for an empty list', () => {
    expect(classifyFilesByExtension([])).toEqual({});
  });

  it('should group files by extension', () => {
    const fileNames = ['file1.txt', 'file2.png', 'file3.txt'];
    const expectedOutput = { txt: ['file1.txt', 'file3.txt'], png: ['file2.png'] };
    expect(classifyFilesByExtension(fileNames)).toEqual(expectedOutput);
  });
});