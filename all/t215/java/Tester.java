package org.real.temp;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.MockitoAnnotations;
import org.mockito.junit.MockitoJUnitRunner;
import org.mockito.stubbing.Answer;

import java.io.BufferedReader;
import java.io.IOException;
import java.util.Map;

import static org.junit.Assert.assertEquals;
import static org.mockito.Mockito.when;

@RunWith(MockitoJUnitRunner.class)
public class Tester {

    @InjectMocks
    private Answer answer; // This seems to be incorrectly used; please verify your intended use

    @Mock
    private BufferedReader mockReader;

    @Test
    public void testReplaceSingleWord() throws IOException {
        String fileContent = "hello world";
        String file_path = "dummy_path.txt";
        Map<String, String> replacementDict = Map.of("hello", "hi");
        String expectedOutput = "hi world";

        when(mockReader.readLine()).thenReturn(fileContent, null);

        String result = replaceWordsInFile(file_path, replacementDict);
        assertEquals(expectedOutput, result);
    }

    @Test
    public void testReplaceMultipleWords() throws IOException {
        String fileContent = "hello world";
        String file_path = "dummy_path.txt";
        Map<String, String> replacementDict = Map.of("hello", "hi", "world", "earth");
        String expectedOutput = "hi earth";

        when(mockReader.readLine()).thenReturn(fileContent, null);

        String result = replaceWordsInFile(file_path, replacementDict);
        assertEquals(expectedOutput, result);
    }

    @Test
    public void testNoReplacement() throws IOException {
        String fileContent = "hello world";
        String file_path = "dummy_path.txt";
        Map<String, String> replacementDict = Map.of("goodbye", "bye");
        String expectedOutput = "hello world";

        when(mockReader.readLine()).thenReturn(fileContent, null);

        String result = replaceWordsInFile(file_path, replacementDict);
        assertEquals(expectedOutput, result);
    }

    @Test
    public void testEmptyFile() throws IOException {
        String fileContent = "";
        String file_path = "dummy_path.txt";
        Map<String, String> replacementDict = Map.of("hello", "hi");
        String expectedOutput = "";

        when(mockReader.readLine()).thenReturn(fileContent, null);

        String result = replaceWordsInFile(file_path, replacementDict);
        assertEquals(expectedOutput, result);
    }
}
