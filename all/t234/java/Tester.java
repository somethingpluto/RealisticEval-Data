package org.real.temp;
import static org.junit.Assert.*;
import org.junit.Before;
import org.junit.Test;
import java.io.*;
import java.util.List;
import java.util.ArrayList;
import com.opencsv.CSVReader;
import static org.real.temp.Answer.*;
public class Tester {

    private StringWriter mockFile;
    private CSVReader reader;

    @Before
    public void setUp() throws IOException {
        // Set up a mock CSV file using StringWriter (similar to StringIO in Python)
        mockFile = new StringWriter();
        mockFile.write("Alice,30,USA\nBob,25,UK\nCharlie,35,Canada\n");
        mockFile.flush(); // Ensure all data is written
        reader = new CSVReader(new StringReader(mockFile.toString()));
    }

    @Test
    public void testAppendNewRow() throws IOException {
        // Test appending a new row when there are no matching values.
        String[] newRow = {"David", "28", "Australia"};
        appendOrSkipRow(mockFile, reader, newRow);

        // Reset the reader and check the contents of the file
        mockFile.flush();
        CSVReader resultReader = new CSVReader(new StringReader(mockFile.toString()));
        List<String[]> result = resultReader.readAll();

        // Check if the new row has been appended
        boolean rowFound = false;
        for (String[] row : result) {
            if (row[0].equals("David") && row[1].equals("28") && row[2].equals("Australia")) {
                rowFound = true;
                break;
            }
        }
        assertTrue("New row should be appended", rowFound);
    }

    @Test
    public void testSkipDifferentValues() throws IOException {
        // Test appending a new row with different values (same name, different age)
        String[] newRow = {"Alice", "31", "USA"};
        appendOrSkipRow(mockFile, reader, newRow);

        // Reset the reader and check the contents of the file
        mockFile.flush();
        CSVReader resultReader = new CSVReader(new StringReader(mockFile.toString()));
        List<String[]> result = resultReader.readAll();

        // Check if the new row has been appended
        boolean rowFound = false;
        for (String[] row : result) {
            if (row[0].equals("Alice") && row[1].equals("31") && row[2].equals("USA")) {
                rowFound = true;
                break;
            }
        }
        assertTrue("Row with different values should be appended", rowFound);
    }

    @Test
    public void testAppendRowWithDifferentColumns() throws IOException {
        // Test appending a row with different values in the first three columns
        String[] newRow = {"Eve", "40", "Australia", "Engineer"};
        appendOrSkipRow(mockFile, reader, newRow);

        // Reset the reader and check the contents of the file
        mockFile.flush();
        CSVReader resultReader = new CSVReader(new StringReader(mockFile.toString()));
        List<String[]> result = resultReader.readAll();

        // Check if the new row with different columns has been appended
        boolean rowFound = false;
        for (String[] row : result) {
            if (row[0].equals("Eve") && row[1].equals("40") && row[2].equals("Australia")) {
                rowFound = true;
                break;
            }
        }
        assertTrue("Row with different columns should be appended", rowFound);
    }

    @Test
    public void testMultipleAppends() throws IOException {
        // Test appending multiple new rows correctly
        String[][] newRows = {
                {"Frank", "29", "Germany"},
                {"Grace", "22", "France"}
        };

        for (String[] row : newRows) {
            appendOrSkipRow(mockFile, reader, row);
            mockFile.flush(); // Reset the file and reader for the next append
            reader = new CSVReader(new StringReader(mockFile.toString()));
        }

        // Reset the reader and check if all rows are appended correctly
        mockFile.flush();
        CSVReader resultReader = new CSVReader(new StringReader(mockFile.toString()));
        List<String[]> result = resultReader.readAll();

        for (String[] row : newRows) {
            boolean rowFound = false;
            for (String[] resultRow : result) {
                if (resultRow[0].equals(row[0]) && resultRow[1].equals(row[1]) && resultRow[2].equals(row[2])) {
                    rowFound = true;
                    break;
                }
            }
            assertTrue("New row should be appended", rowFound);
        }
    }
}
