package org.real.temp;

import static org.junit.Assert.assertEquals;
import static org.mockito.Mockito.*;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

import org.junit.Before;
import org.junit.Test;
import org.mockito.Mock;
import org.mockito.MockitoAnnotations;

public class Tester {

    @Mock
    private BufferedReader mockBufferedReader;

    @Before
    public void setUp() {
        MockitoAnnotations.initMocks(this);
    }

    @Test
    public void testCsvToSqlInsert() throws IOException {
        String csvFilePath = "path/to/your/csvfile.csv";

        when(mockBufferedReader.readLine()).thenReturn("column1,column2", "value1,value2", null);

        Files.createFile(Paths.get(csvFilePath));
        try (FileWriter writer = new FileWriter(csvFilePath)) {
            writer.write("column1,column2\n");
            writer.write("value1,value2\n");
        }

        // Call the method under test
        String result = csvToSqlInsert(csvFilePath);

        // Verify the expected output
        assertEquals("INSERT INTO tablename (column1, column2) VALUES ('value1', 'value2');\n", result);

        // Clean up
        Files.deleteIfExists(Paths.get(csvFilePath));
    }

    private String csvToSqlInsert(String csvFilePath) throws IOException {
        StringBuilder sb = new StringBuilder();
        try (BufferedReader br = new BufferedReader(new FileReader(csvFilePath))) {
            String line;
            while ((line = br.readLine()) != null) {
                if (sb.length() > 0) {
                    sb.append("\n");
                }
                String[] columns = line.split(",");
                String tableName = Paths.get(csvFilePath).getFileName().toString().replace(".csv", "");
                sb.append("INSERT INTO ").append(tableName).append(" (").append(String.join(", ", columns)).append(") VALUES (")
                        .append(String.join(", '", Arrays.stream(columns).map(s -> "'" + s + "'").toArray(String[]::new))).append(");");
            }
        }
        return sb.toString();
    }
}