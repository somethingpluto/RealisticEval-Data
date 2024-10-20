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
import java.util.HashMap;
import java.util.Map;

import static org.junit.Assert.assertEquals;
import static org.real.temp.Answer.*;

public class Tester {

    private Map<String, String> testFiles = new HashMap<String, String>() {{
        put("test1.csv", "id,name,age\n1,Alice,30\n2,Bob,25");
        put("test2.csv", "product_id,product_name,price\n101,Widget,9.99\n102,Gadget,12.49");
        put("test3.csv", "user_id,email\n3,test@example.com\n4,user@domain.com");
        put("test4.csv", "order_id,order_date,total\n1001,2024-09-01,59.99");
        put("test5.csv", "quote_id,quote\n1,\"It's a beautiful day.\"\n2,\"She said, \"\"Hello!\"\"\"");
    }};

    private Path tempDir;

    @Before
    public void setUp() throws IOException {
        // Create a temporary directory
        tempDir = Files.createTempDirectory("tempDir");

        // Create the sample CSV files in the temporary directory
        for (Map.Entry<String, String> entry : testFiles.entrySet()) {
            File file = tempDir.resolve(entry.getKey()).toFile();
            try (FileWriter writer = new FileWriter(file)) {
                writer.write(entry.getValue());
            }
        }
    }

    @After
    public void tearDown() throws IOException {
        // Delete the temporary directory and its contents
        Files.walk(tempDir)
                .sorted((path1, path2) -> path2.compareTo(path1)) // Sort in reverse order to delete files before directories
                .map(Path::toFile)
                .forEach(File::delete);
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
        String expectedSql = "INSERT INTO 'test4' (order_id, order_date, total) VALUES ('1001', '2024-09-01', '59.99');";

        String result = csvToSqlInsert(tempDir.resolve("test4.csv").toString());
        assertEquals(expectedSql, result);
    }
}
