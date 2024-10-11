package org.real.temp;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.mockito.Mockito.*;

import java.io.File;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.Mock;
import org.mockito.MockitoAnnotations;

public class Tester {

    @Mock
    private BibExtractor bibExtractor;

    @BeforeEach
    public void setUp() {
        MockitoAnnotations.openMocks(this);
    }

    @Test
    public void testExtractBibInfo() {
        // Arrange
        String bibFilePath = "path/to/bibtex/file.bib";
        List<Map<String, String>> expectedOutput = Arrays.asList(
            Map.of("title", "A Comprehensive Study on AI", "author", "John Doe and Jane Smith", "year", "2024")
        );

        when(bibExtractor.extractBibInfo(anyString())).thenReturn(expectedOutput);

        // Act
        List<Map<String, String>> actualOutput = bibExtractor.extractBibInfo(bibFilePath);

        // Assert
        assertEquals(expectedOutput, actualOutput);
    }
}