import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;
import org.mockito.stubbing.Answer;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.mockito.Mockito.when;
import static org.mockito.Mockito.mock;

@ExtendWith(MockitoExtension.class)
public class Tester {

    @Mock
    private BufferedReader mockReader;

    @InjectMocks
    private Answer answer;

    @BeforeEach
    public void setUp() {
        // Setup any common mocks or initializations here
    }

    @Test
    public void testReadCorrectData() throws IOException {
        // Mock the BufferedReader to simulate reading correct data
        String mockFileContent = "{\"test_acc1\": 88.5, \"train_loss\": 0.75}\n" +
                                 "{\"test_acc1\": 89.0, \"train_loss\": 0.70}";
        when(mockReader.readLine()).thenAnswer((Answer<String>) invocation -> {
            for (String line : mockFileContent.split("\n")) {
                if (!line.isEmpty()) {
                    yield line;
                }
            }
            yield null;
        });

        List<Double> trainLossList;
        List<Double> testAcc1List;

        try {
            trainLossList = new ArrayList<>();
            testAcc1List = new ArrayList<>();
            answer.readLog("dummy_path.json", trainLossList, testAcc1List);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }

        assertEquals(List.of(0.75, 0.70), trainLossList);
        assertEquals(List.of(88.5, 89.0), testAcc1List);
    }

    @Test
    public void testReadCorrectDataSingle() throws IOException {
        // Mock the BufferedReader to simulate reading a single correct data line
        String mockFileContent = "{\"test_acc1\": 88.5, \"train_loss\": 0.75}";
        when(mockReader.readLine()).thenReturn(mockFileContent, (String) null);

        List<Double> trainLossList;
        List<Double> testAcc1List;

        try {
            trainLossList = new ArrayList<>();
            testAcc1List = new ArrayList<>();
            answer.readLog("dummy_path.json", trainLossList, testAcc1List);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }

        assertEquals(List.of(0.75), trainLossList);
        assertEquals(List.of(88.5), testAcc1List);
    }

    @Test
    public void testEmptyFile() throws IOException {
        // Mock the BufferedReader to simulate reading an empty file
        when(mockReader.readLine()).thenReturn((String) null);

        List<Double> trainLossList;
        List<Double> testAcc1List;

        try {
            trainLossList = new ArrayList<>();
            testAcc1List = new ArrayList<>();
            answer.readLog("empty_file.json", trainLossList, testAcc1List);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }

        assertEquals(List.of(), trainLossList);
        assertEquals(List.of(), testAcc1List);
    }

    @Test
    public void testPartialDataEntries() throws IOException {
        // Mock the BufferedReader to simulate reading partial data entries
        String mockFileContent = "{\"test_acc1\": 88.5, \"train_loss\": 0.75}\n" +
                                 "{\"test_acc1\": 90.0,\"train_loss\": 0.75,\"f1\":0.91}";
        when(mockReader.readLine()).thenAnswer((Answer<String>) invocation -> {
            for (String line : mockFileContent.split("\n")) {
                if (!line.isEmpty()) {
                    yield line;
                }
            }
            yield null;
        });

        List<Double> trainLossList;
        List<Double> testAcc1List;

        try {
            trainLossList = new ArrayList<>();
            testAcc1List = new ArrayList<>();
            answer.readLog("partial_data_file.json", trainLossList, testAcc1List);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }

        assertEquals(List.of(0.75, 0.75), trainLossList);
        assertEquals(List.of(88.5, 90.0), testAcc1List);
    }
}
