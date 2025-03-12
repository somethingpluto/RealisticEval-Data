import { promisify } from 'util';
import { readdir } from 'fs';
import { join } from 'path';

const readdirAsync = promisify(readdir);

async function classifyFilesByExtensionInDirectory(directoryPath: string): Promise<{[key: string]: string[]}> {
  try {
    const files = await readdirAsync(directoryPath);
    const fileNames = files.filter(file => file.endsWith('.txt') || file.endsWith('.md'));
    return classifyFilesByExtension(fileNames);
  } catch (error) {
    console.error('Error reading directory:', error);
    return {};
  }
}
describe('classifyFilesByExtension', () => {
  it('should correctly classify files with multiple file types', () => {
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

  it('should handle an empty list of file names', () => {
      const files = [];
      const expectedResult = {};
      expect(classifyFilesByExtension(files)).toEqual(expectedResult);
  });

  it('should correctly classify files with the same extension', () => {
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

  it('should correctly classify files with multiple dots in their names', () => {
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
