npm install docx
const { Document } = require('docx');
const fs = require('fs');

describe('TestExtractTextFromWord', () => {
    let testDocxPath;

    beforeEach(() => {
        testDocxPath = "test_document.docx";
        createSampleDocx(testDocxPath);
    });

    afterEach(() => {
        if (fs.existsSync(testDocxPath)) {
            fs.unlinkSync(testDocxPath);
        }
    });

    function createSampleDocx(path) {
        const doc = new Document();
        doc.addParagraph("Hello World!");
        doc.addParagraph("This is a test document.");
        doc.save(path);
    }

    it('should extract text from a normal Word document', async () => {
        const expectedText = "Hello World!\nThis is a test document.";
        const extractedText = await extractTextFromWord(testDocxPath);
        expect(extractedText.trim()).toEqual(expectedText);
    });

    it('should extract text from an empty Word document', async () => {
        const emptyDocxPath = "empty_document.docx";
        new Document().save(emptyDocxPath);

        const extractedText = await extractTextFromWord(emptyDocxPath);
        expect(extractedText).toEqual("");  // Expecting an empty string

        fs.unlinkSync(emptyDocxPath);  // Clean up
    });

    it('should extract text from a document containing special characters', async () => {
        const specialDocxPath = "special_characters.docx";
        const doc = new Document();
        doc.addParagraph("Hello, 世界! @#$%^&*()");
        doc.save(specialDocxPath);

        const extractedText = await extractTextFromWord(specialDocxPath);
        const expectedText = "Hello, 世界! @#$%^&*()";
        expect(extractedText.trim()).toEqual(expectedText);

        fs.unlinkSync(specialDocxPath);  // Clean up
    });

    it('should extract text from a document with multiple paragraphs', async () => {
        const multiParaDocxPath = "multi_paragraphs.docx";
        const doc = new Document();
        doc.addParagraph("First paragraph.");
        doc.addParagraph("Second paragraph.");
        doc.addParagraph("Third paragraph.");
        doc.save(multiParaDocxPath);

        const extractedText = await extractTextFromWord(multiParaDocxPath);
        const expectedText = "First paragraph.\nSecond paragraph.\nThird paragraph.";
        expect(extractedText.trim()).toEqual(expectedText);

        fs.unlinkSync(multiParaDocxPath);  // Clean up
    });
});

