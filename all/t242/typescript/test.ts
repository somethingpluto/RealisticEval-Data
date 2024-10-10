describe('classifyFilesByExtension', () => {
  it('should return an empty object for an empty array', () => {
    const result = classifyFilesByExtension([]);
    expect(result).toEqual({});
  });

  it('should group files by extension', () => {
    const result = classifyFilesByExtension(['file1.txt', 'file2.jpg', 'file3.txt']);
    expect(result).toEqual({
      '.txt': ['file1.txt', 'file3.txt'],
      '.jpg': ['file2.jpg']
    });
  });
});