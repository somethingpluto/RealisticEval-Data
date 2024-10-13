package org.real.temp;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

import static org.junit.Assert.assertEquals;


public class Tester {

    private Map<String, String> testFiles = Map.of(
        "test1.csv", "id,name,age\n1,Alice,30\n2,Bob,25",
        "test2.csv", "product_id,product_name,price\n101,Widget,9.99\n102,Gadget,12.49",
        "test3.csv", "user_id,email\n3,test@example.com\n4,user@domain.com",
        "test4.csv", "order_id,order_date,total\n1001,2024-09-01,59.99",
        "test5.csv", "quote_id,quote\n1,\"It's a beautiful day.\"\n2,\"She said, \"\"Hello!\"\"\""
    );

    @TempDir
    Path tempDir;

    @BeforeEach
    public void setUp() throws IOException {
        // Create the sample CSV files in the temporary directory
        for (Map.Entry<String, String> entry : testFiles.entrySet()) {
            File file = tempDir.resolve(entry.getKey()).toFile();
            try (FileWriter writer = new FileWriter(file)) {
                writer.write(entry.getValue());
            }
        }
    }

    @AfterEach
    public void tearDown() {
        // No need to manually delete files as they are in a temporary directory
    }

    @Test
    public void testSimpleCsv() throws IOException {
        String expectedSql = "INSERT INTO test1 (id, name, age) VALUES ('1', 'Alice', '30');\n"
                + "INSERT INTO test1 (id, name, age) VALUES ('2', 'Bob', '25');";

        String result = csvToSqlInsert(tempDir.resolve("test1.csv").toString());
        assertEquals(expectedSql, result);
    }

    @Test
    public void testProductCsv() throws IOException {
        String expectedSql = "INSERT INTO test2 (product_id, product_name, price) VALUES ('101', 'Widget', '9.99');\n"
                + "INSERT INTO test2 (product_id, product_name, price) VALUES ('102', 'Gadget', '12.49');";

        String result = csvToSqlInsert(tempDir.resolve("test2.csv").toString());
        assertEquals(expectedSql, result);
    }

    @Test
    public void testEmailCsv() throws IOException {
        String expectedSql = "INSERT INTO test3 (user_id, email) VALUES ('3', 'test@example.com');\n"
                + "INSERT INTO test3 (user_id, email) VALUES ('4', 'user@domain.com');";

        String result = csvToSqlInsert(tempDir.resolve("test3.csv").toString());
        assertEquals(expectedSql, result);
    }

    @Test
    public void testDateAndDecimalCsv() throws IOException {
        String expectedSql = "INSERT INTO test4 (order_id, order_date, total) VALUES ('1001', '2024-09-01', '59.99');";

        String result = csvToSqlInsert(tempDir.resolve("test4.csv").toString());
        assertEquals(expectedSql, result);
    }

    // Utility method to convert CSV to SQL insert statements
    public static String csvToSqlInsert(String csvFilePath) {
        // Extract the table name from the CSV file name, removing the suffix
        Path path = Paths.get(csvFilePath);
        String tableName = path.getFileName().toString().replaceFirst("[.][^.]+$", "");

        // Open the CSV file and read its contents
        List<String> insertStatements = new ArrayList<>();
        try (BufferedReader reader = new BufferedReader(new FileReader(csvFilePath))) {
            String line = reader.readLine(); // Skip the first line (header)
            if (line != null) {
                String[] headers = line.split(",");
                
                String currentLine;
                while ((currentLine = reader.readLine()) != null) {
                    String[] row = currentLine.split(",");
                    List<String> values = new ArrayList<>();
                    
                    for (String value : row) {
                        // Handle different types of values (e.g., strings, numbers)
                        if (value.matches("\\d+")) {  // If value is a digit, no quotes needed
                            values.add(value);
                        } else {  // Assume it's a string otherwise
                            String escapedValue = value.replace("'", "''");  // Escape single quotes
                            values.add("'" + escapedValue + "'");  // Use double quotes outside
                        }
                    }

                    // Join column names and values to form an INSERT statement
                    String insertStatement = String.format("INSERT INTO %s (%s) VALUES (%s);",
                            tableName,
                            String.join(", ", headers),
                            String.join(", ", values));
                    insertStatements.add(insertStatement);
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        // Combine all insert statements into a single output
        return String.join("\n", insertStatements);
    }
}

public class Tester {

    private Map<String, String> testFiles = Map.of(
        "test1.csv", "id,name,age\n1,Alice,30\n2,Bob,25",
        "test2.csv", "product_id,product_name,price\n101,Widget,9.99\n102,Gadget,12.49",
        "test3.csv", "user_id,email\n3,test@example.com\n4,user@domain.com",
        "test4.csv", "order_id,order_date,total\n1001,2024-09-01,59.99",
        "test5.csv", "quote_id,quote\n1,\"It's a beautiful day.\"\n2,\"She said, \"\"Hello!\"\"\""
    );

    @TempDir
    Path tempDir;

    @BeforeEach
    public void setUp() throws IOException {
        // Create the sample CSV files in the temporary directory
        for (Map.Entry<String, String> entry : testFiles.entrySet()) {
            File file = tempDir.resolve(entry.getKey()).toFile();
            try (FileWriter writer = new FileWriter(file)) {
                writer.write(entry.getValue());
            }
        }
    }

    @AfterEach
    public void tearDown() {
        // No need to manually delete files as they are in a temporary directory
    }

    @Test
    public void testSimpleCsv() throws IOException {
        String expectedSql = "INSERT INTO test1 (id, name, age) VALUES ('1', 'Alice', '30');\n"
                + "INSERT INTO test1 (id, name, age) VALUES ('2', 'Bob', '25');";

        String result = csvToSqlInsert(tempDir.resolve("test1.csv").toString());
        assertEquals(expectedSql, result);
    }

    @Test
    public void testProductCsv() throws IOException {
        String expectedSql = "INSERT INTO test2 (product_id, product_name, price) VALUES ('101', 'Widget', '9.99');\n"
                + "INSERT INTO test2 (product_id, product_name, price) VALUES ('102', 'Gadget', '12.49');";

        String result = csvToSqlInsert(tempDir.resolve("test2.csv").toString());
        assertEquals(expectedSql, result);
    }

    @Test
    public void testEmailCsv() throws IOException {
        String expectedSql = "INSERT INTO test3 (user_id, email) VALUES ('3', 'test@example.com');\n"
                + "INSERT INTO test3 (user_id, email) VALUES ('4', 'user@domain.com');";

        String result = csvToSqlInsert(tempDir.resolve("test3.csv").toString());
        assertEquals(expectedSql, result);
    }

    @Test
    public void testDateAndDecimalCsv() throws IOException {
        String expectedSql = "INSERT INTO test4 (order_id, order_date, total) VALUES ('1001', '2024-09-01', '59.99');";

        String result = csvToSqlInsert(tempDir.resolve("test4.csv").toString());
        assertEquals(expectedSql, result);
    }

    // Utility method to convert CSV to SQL insert statements
    public static String csvToSqlInsert(String csvFilePath) {
        // Extract the table name from the CSV file name, removing the suffix
        Path path = Paths.get(csvFilePath);
        String tableName = path.getFileName().toString().replaceFirst("[.][^.]+$", "");

        // Open the CSV file and read its contents
        List<String> insertStatements = new ArrayList<>();
        try (BufferedReader reader = new BufferedReader(new FileReader(csvFilePath))) {
            String line = reader.readLine(); // Skip the first line (header)
            if (line != null) {
                String[] headers = line.split(",");
                
                String currentLine;
                while ((currentLine = reader.readLine()) != null) {
                    String[] row = currentLine.split(",");
                    List<String> values = new ArrayList<>();
                    
                    for (String value : row) {
                        // Handle different types of values (e.g., strings, numbers)
                        if (value.matches("\\d+")) {  // If value is a digit, no quotes needed
                            values.add(value);
                        } else {  // Assume it's a string otherwise
                            String escapedValue = value.replace("'", "''");  // Escape single quotes
                            values.add("'" + escapedValue + "'");  // Use double quotes outside
                        }
                    }

                    // Join column names and values to form an INSERT statement
                    String insertStatement = String.format("INSERT INTO %s (%s) VALUES (%s);",
                            tableName,
                            String.join(", ", headers),
                            String.join(", ", values));
                    insertStatements.add(insertStatement);
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        // Combine all insert statements into a single output
        return String.join("\n", insertStatements);
    }
}