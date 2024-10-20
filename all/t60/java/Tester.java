package org.real.temp;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

import static org.real.temp.Answer.*;

import static org.junit.Assert.assertEquals;

public class Tester {

    private static final String TEST_DIR = "test_dir";

    @Before
    public void setUp() throws IOException {
        // Set up a temporary directory
        Files.createDirectories(new File(TEST_DIR).toPath());
    }

    @After
    public void tearDown() throws IOException {
        // Remove created files and directory after each test
        File dir = new File(TEST_DIR);
        File[] files = dir.listFiles();
        if (files != null) {
            for (File file : files) {
                file.delete();
            }
        }
        dir.delete();
    }

    @Test
    public void testAllSameColumns() throws IOException {
        // All CSV files have the same columns
        String data1 = "A,B,C\n1,2,3";
        String data2 = "A,B,C\n4,5,6";
        String data3 = "A,B,C\n7,8,9";
        List<String> filenames = Arrays.asList("file1.csv", "file2.csv", "file3.csv");
        List<String> datas = Arrays.asList(data1, data2, data3);

        writeFiles(filenames, datas);

        assertEquals(Arrays.asList("A", "B", "C"), findCommonColumns(TEST_DIR));
    }

    @Test
    public void testNoCommonColumns() throws IOException {
        // No common columns
        String data1 = "A,B,C\n1,2,3";
        String data2 = "D,E,F\n4,5,6";
        String data3 = "G,H,I\n7,8,9";
        List<String> filenames = Arrays.asList("file1.csv", "file2.csv", "file3.csv");
        List<String> datas = Arrays.asList(data1, data2, data3);

        writeFiles(filenames, datas);

        assertEquals(List.of(), findCommonColumns(TEST_DIR));
    }

    @Test
    public void testSomeCommonColumns() throws IOException {
        // Some common columns
        String data1 = "A,B,C\n1,2,3";
        String data2 = "B,C,D\n4,5,6";
        String data3 = "C,D,E\n7,8,9";
        List<String> filenames = Arrays.asList("file1.csv", "file2.csv", "file3.csv");
        List<String> datas = Arrays.asList(data1, data2, data3);

        writeFiles(filenames, datas);

        assertEquals(List.of("C"), findCommonColumns(TEST_DIR));
    }

    @Test
    public void testMixedCommonAndUniqueColumns() throws IOException {
        // Mixed common and unique columns
        String data1 = "A,B,C\n1,2,3";
        String data2 = "B,C,D\n4,5,6";
        String data3 = "B,C,E\n7,8,9";
        List<String> filenames = Arrays.asList("file1.csv", "file2.csv", "file3.csv");
        List<String> datas = Arrays.asList(data1, data2, data3);

        writeFiles(filenames, datas);

        assertEquals(Arrays.asList("B", "C"), findCommonColumns(TEST_DIR));
    }

    private void writeFiles(List<String> filenames, List<String> datas) throws IOException {
        for (int i = 0; i < filenames.size(); i++) {
            String filename = filenames.get(i);
            String data = datas.get(i);
            File file = new File(TEST_DIR, filename);
            try (FileWriter writer = new FileWriter(file)) {
                writer.write(data);
            }
        }
    }
}
