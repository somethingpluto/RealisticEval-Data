import { Document } from 'docx';

describe('TestExtractTextFromWord', () => {
  let testDocxPath: string;

  beforeEach(() => {
    // Set up the testing environment
    testDocxPath = 'test_document.docx';
    createSampleDocx();
  });

  afterEach(() => {
    // Clean up the test environment
    if (require('fs').existsSync(testDocxPath)) {
      require('fs').unlinkSync(testDocxPath);
    }
  });

  function createSampleDocx() {
    // Helper method to create a sample Word document for testing
    const doc = new Document();
    doc.addParagraph('Hello World!');
    doc.addParagraph('This is a test document.');
    doc.save(testDocxPath);
  }

  it('should extract text from a normal Word document', () => {
    const expectedText = 'Hello World!\nThis is a test document.';
    const extractedText = extractTextFromWord(testDocxPath);
    expect(extractedText.trim()).toEqual(expectedText);
  });

  it('should extract text from an empty Word document', () => {
    const emptyDocxPath = 'empty_document.docx';
    new Document().save(emptyDocxPath);

    const extractedText = extractTextFromWord(emptyDocxPath);
    expect(extractedText).toEqual('');

    require('fs').unlinkSync(emptyDocxPath); // Clean up
  });

  it('should extract text from a document containing special characters', () => {
    const specialDocxPath = 'special_characters.docx';
    const doc = new Document();
    doc.addParagraph('Hello, 世界! @#$%^&*()');
    doc.save(specialDocxPath);

    const extractedText = extractTextFromWord(specialDocxPath);
    const expectedText = 'Hello, 世界! @#$%^&*()';
    expect(extractedText.trim()).toEqual(expectedText);

    require('fs').unlinkSync(specialDocxPath); // Clean up
  });

  it('should extract text from a document with multiple paragraphs', () => {
    const multiParaDocxPath = 'multi_paragraphs.docx';
    const doc = new Document();
    doc.addParagraph('First paragraph.');
    doc.addParagraph('Second paragraph.');
    doc.addParagraph('Third paragraph.');
    doc.save(multiParaDocxPath);

    const extractedText = extractTextFromWord(multiParaDocxPath);
    const expectedText = 'First paragraph.\nSecond paragraph.\nThird paragraph.';
    expect(extractedText.trim()).toEqual(expectedText);

    require('fs').unlinkSync(multiParaDocxPath); // Clean up
  });
});