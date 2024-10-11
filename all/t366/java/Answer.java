import org.apache.poi.xwpf.usermodel.XWPFDocument;
import org.apache.poi.xwpf.usermodel.XWPFParagraph;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;

public class Answer {

    public static String extractTextFromWord(String docxFilePath) throws IOException {
        FileInputStream fis = new FileInputStream(new File(docxFilePath));
        XWPFDocument document = new XWPFDocument(fis);

        StringBuilder stringBuilder = new StringBuilder();
        for(XWPFParagraph paragraph : document.getParagraphs()) {
            stringBuilder.append(paragraph.getText());
        }

        fis.close();
        return stringBuilder.toString();
    }

}