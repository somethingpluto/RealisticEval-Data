/**
 * Classify an array of file names according to their file extensions.
 *
 * @param {string[]} fileNames - List of file names (strings).
 * @returns {Object} - Dictionary with file extensions as keys and lists of file names as values.
 */
function classifyFilesByExtension(fileNames) {
    const fileDict = {};

    fileNames.forEach(fileName => {
        const extension = fileName.split('.').pop();
        if (!fileDict[extension]) {
            fileDict[extension] = [];
        }
        fileDict[extension].push(fileName);
    });

    return fileDict;
}
describe('TestClassifyFilesByExtension', () => {
  it('test with multiple file types', () => {
      const files = [
          "document.docx",
          "photo.jpeg",
          "report.pdf",
          "image.png",
          "archive.zip"
      ];
      const expectedResult = {
          'docx': ['document.docx'],
          'jpeg': ['photo.jpeg'],
          'pdf': ['report.pdf'],
          'png': ['image.png'],
          'zip': ['archive.zip']
      };
      expect(classifyFilesByExtension(files)).toEqual(expectedResult);
  });

  it('test with an empty list of file names', () => {
      const files = [];
      const expectedResult = {};
      expect(classifyFilesByExtension(files)).toEqual(expectedResult);
  });

  it('test with multiple files having the same extension', () => {
      const files = [
          "file1.txt",
          "file2.txt",
          "file3.txt",
      ];
      const expectedResult = {
          'txt': [
              "file1.txt",
              "file2.txt",
              "file3.txt",
          ]
      };
      expect(classifyFilesByExtension(files)).toEqual(expectedResult);
  });

  it('test files that have multiple dots in their names', () => {
      const files = [
          "my.document.docx",
          "report.final.pdf",
          "photo.album.jpeg",
          "archive.backup.zip"
      ];
      const expectedResult = {
          'docx': ['my.document.docx'],
          'pdf': ['report.final.pdf'],
          'jpeg': ['photo.album.jpeg'],
          'zip': ['archive.backup.zip']
      };
      expect(classifyFilesByExtension(files)).toEqual(expectedResult);
  });
});
