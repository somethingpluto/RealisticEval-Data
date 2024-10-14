package org.real.temp;

import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.mockito.Mock;
import org.mockito.runners.MockitoJUnitRunner;

import java.io.ByteArrayInputStream;
import java.io.InputStream;
import java.util.List;

import static org.junit.Assert.assertEquals;
import static org.mockito.Mockito.when;

@ExtendWith(MockitoExtension.class)
public class Tester {

    @Mock
    private InputStream mockStdin;

    @BeforeEach
    void setUp() {
        // Set up the mock standard input stream
        System.setIn(mockStdin);
    }

    @Test
    void testBasicTsvInput() {
        String input = "col1\tcol2\tcol3\nval1\tval2\tval3\n";
        when(mockStdin.readAllBytes()).thenReturn(input.getBytes());

        List<List<String>> expectedOutput = List.of(
            List.of("col1", "col2", "col3"),
            List.of("val1", "val2", "val3")
        );

        List<List<String>> actualOutput = readTsvFromStdin();

        assertEquals(expectedOutput, actualOutput);
    }

    @Test
    void testSingleColumn() {
        String input = "col1\nval1\nval2\n";
        when(mockStdin.readAllBytes()).thenReturn(input.getBytes());

        List<List<String>> expectedOutput = List.of(
            List.of("col1"),
            List.of("val1"),
            List.of("val2")
        );

        List<List<String>> actualOutput = readTsvFromStdin();

        assertEquals(expectedOutput, actualOutput);
    }
}