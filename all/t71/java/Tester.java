import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

import java.io.File;
import java.util.Arrays;

public class FileReaderTest {

    private FileReader fileReader;

    @BeforeEach
    public void setUp() {
        fileReader = new FileReader();
    }

    @Test
    public void testReadColumns() throws Exception {
        // Assuming the file 'test.txt' exists in the resources directory
        File file = new File("src/test/resources/test.txt");
        double[][] expected = {{1.0, 2.0}, {3.0, 4.0}};
        double[][] result = fileReader.readColumns(file.getAbsolutePath());

        assertArrayEquals(expected, result);
    }
}
