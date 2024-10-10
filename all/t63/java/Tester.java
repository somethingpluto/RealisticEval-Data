package org.real.temp;

import static org.junit.Assert.assertEquals;
import org.junit.Before;
import org.junit.Test;
import org.apache.commons.csv.CSVFormat;
import org.apache.commons.csv.CSVPrinter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

public class Tester {

    private String tempFilePath = "temp.md";

    @Before
    public void setUp() throws IOException {
        // Clean up any existing temporary files
        try {
            new FileWriter(tempFilePath).close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    @Test
    public void test_dataframe_to_markdown() throws IOException {
        Map<String, Object> data = new HashMap<>();
        data.put("Name", new String[]{"Alice", "Bob"});
        data.put("Age", new Integer[]{25, 30});

        String markdownContent = dataframeToMarkdown(data);

        assertEquals("| Name | Age |\n| --- | --- |\n| Alice | 25 |\n| Bob | 30 |\n", markdownContent);
    }

    private String dataframeToMarkdown(Map<String, Object> data) throws IOException {
        StringBuilder sb = new StringBuilder();
        CSVPrinter csvPrinter = null;

        try (FileWriter out = new FileWriter(tempFilePath)) {
            csvPrinter = new CSVPrinter(out, CSVFormat.DEFAULT.withHeader((String[]) data.keySet().toArray()));
            for (int i = 0; i < ((Object[]) data.get("Name")).length; i++) {
                csvPrinter.printRecord(((Object[]) data.get("Name"))[i], ((Integer[]) data.get("Age"))[i]);
            }
        } finally {
            if (csvPrinter != null) {
                csvPrinter.close();
            }
        }

        return sb.toString();
    }
}