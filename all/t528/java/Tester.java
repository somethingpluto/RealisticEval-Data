package org.real.temp;

import static org.mockito.Mockito.*;
import static org.junit.Assert.*;

import org.junit.Before;
import org.junit.Test;
import org.mockito.Mockito;

import java.io.File;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class Tester {

    @Before
    public void setUp() {
        // Clear all mocks before each test
        Mockito.reset();
    }

    @Test
    public void shouldReturnEmptyListForEmptyDirectory() {
        File mockDir = mock(File.class);
        when(mockDir.listFiles()).thenReturn(new File[0]);

        List<String> result = MarkdownFinder.findMarkdownFiles(mockDir.getAbsolutePath());
        assertEquals(Collections.emptyList(), result);
    }

    @Test
    public void shouldReturnListWithOneMarkdownFile() {
        File mockDir = mock(File.class);
        File mockFile = mock(File.class);
        when(mockDir.listFiles()).thenReturn(new File[]{mockFile});
        when(mockFile.getName()).thenReturn("file1.md");
        when(mockFile.isDirectory()).thenReturn(false);

        List<String> result = MarkdownFinder.findMarkdownFiles(mockDir.getAbsolutePath());
        assertEquals(Arrays.asList("dir\\file1.md"), result);
    }

    @Test
    public void shouldReturnListWithMultipleMarkdownFilesInSameDirectory() {
        File mockDir = mock(File.class);
        File mockFile1 = mock(File.class);
        File mockFile2 = mock(File.class);
        when(mockDir.listFiles()).thenReturn(new File[]{mockFile1, mockFile2});
        when(mockFile1.getName()).thenReturn("file1.md");
        when(mockFile2.getName()).thenReturn("file2.md");
        when(mockFile1.isDirectory()).thenReturn(false);
        when(mockFile2.isDirectory()).thenReturn(false);

        List<String> result = MarkdownFinder.findMarkdownFiles(mockDir.getAbsolutePath());
        assertEquals(Arrays.asList("dir\\file1.md", "dir\\file2.md"), result);
    }

    @Test
    public void shouldReturnMarkdownFilesIgnoringNonMarkdownFiles() {
        File mockDir = mock(File.class);
        File mockFile1 = mock(File.class);
        File mockFile2 = mock(File.class);
        File mockFile3 = mock(File.class);
        when(mockDir.listFiles()).thenReturn(new File[]{mockFile1, mockFile2, mockFile3});
        when(mockFile1.getName()).thenReturn("file1.txt");
        when(mockFile2.getName()).thenReturn("file2.md");
        when(mockFile3.getName()).thenReturn("file3.doc");
        when(mockFile1.isDirectory()).thenReturn(false);
        when(mockFile2.isDirectory()).thenReturn(false);
        when(mockFile3.isDirectory()).thenReturn(false);

        List<String> result = MarkdownFinder.findMarkdownFiles(mockDir.getAbsolutePath());
        assertEquals(Arrays.asList("dir\\file2.md"), result);
    }

    @Test
    public void shouldHandleDirectoryWithOnlyNonMarkdownFiles() {
        File mockDir = mock(File.class);
        File mockFile1 = mock(File.class);
        File mockFile2 = mock(File.class);
        when(mockDir.listFiles()).thenReturn(new File[]{mockFile1, mockFile2});
        when(mockFile1.getName()).thenReturn("file1.txt");
        when(mockFile2.getName()).thenReturn("file2.doc");
        when(mockFile1.isDirectory()).thenReturn(false);
        when(mockFile2.isDirectory()).thenReturn(false);

        List<String> result = MarkdownFinder.findMarkdownFiles(mockDir.getAbsolutePath());
        assertEquals(Collections.emptyList(), result);
    }
}