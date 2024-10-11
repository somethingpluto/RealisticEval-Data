package org.real.temp;

import org.apache.pdfbox.pdmodel.PDDocument;
import org.apache.pdfbox.text.PDFTextStripper;

import java.io.File;
import java.io.IOException;

public class Answer {

    /**
     * Extracts text from a given PDF file.
     *
     * @param filePath The path to the PDF file from which to extract text.
     * @return The extracted text from the PDF.
     */
    public static String extractTextFromPdf(String filePath) {
        try (PDDocument document = PDDocument.load(new File(filePath))) {
            if (!document.isEncrypted()) {
                PDFTextStripper pdfStripper = new PDFTextStripper();
                return pdfStripper.getText(document);
            } else {
                throw new IOException("PDF is encrypted and cannot be read.");
            }
        } catch (IOException e) {
            e.printStackTrace();
            return null;
        }
    }

    public static void main(String[] args) {
        // Example usage
        String filePath = "path/to/your/pdf/file.pdf";
        String extractedText = extractTextFromPdf(filePath);
        System.out.println(extractedText);
    }
}