import static org.junit.jupiter.api.Assertions.*;
import java.io.File;
import java.util.List;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

public class TesterTest {

    private Tester tester;

    @BeforeEach
    public void setUp() {
        tester = new Tester();
    }

    @Test
    public void testExtractParseDicts() throws Exception {
        // Arrange
        File file = new File("path/to/your/file.txt"); // Replace with actual file path
        String expectedOutput = "[{\"key1\": \"value1\", \"key2\": \"value2\"}, {\"key3\": \"value3\"}]"; // Replace with expected output

        // Act
        List<String> result = tester.extractParseDicts(file.getAbsolutePath());

        // Assert
        assertEquals(expectedOutput, result.toString());
    }
}