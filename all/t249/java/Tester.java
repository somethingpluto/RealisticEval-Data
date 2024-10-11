package org.real.temp;

import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;

public class Tester {

    @Test
    public void testExtractTextFromPdf() {
        // Arrange
        String filePath = "path/to/your/pdf/file.pdf";
        PdfExtractor pdfExtractor = new PdfExtractor();

        // Act
        String extractedText = pdfExtractor.extractTextFromPdf(filePath);

        // Assert
        assertEquals("Expected Text", extractedText); // Replace "Expected Text" with the actual expected output
    }
}