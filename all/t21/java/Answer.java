package org.real.temp;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Answer {

    /**
     * Compare the contents of two files and print the differences in unified diff format.
     *
     * @param file1Path Path to the first file.
     * @param file2Path Path to the second file.
     * @return A list containing the lines of differences, if any.
     * @throws java.io.FileNotFoundException If either file does not exist.
     * @throws java.io.IOException If there is an error reading the files.
     */
    public static List<String> compareFiles(String file1Path, String file2Path) throws java.io.FileNotFoundException, IOException {
        List<String> lines1 = readFile(file1Path);
        List<String> lines2 = readFile(file2Path);

        List<String> diffLines = unifiedDiff(lines1, lines2, file1Path, file2Path);

        // Print the differences
        for (String line : diffLines) {
            System.out.print(line);
        }

        return diffLines;
    }

    private static List<String> readFile(String filePath) throws java.io.FileNotFoundException, IOException {
        List<String> lines = new ArrayList<>();
        try (BufferedReader reader = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = reader.readLine()) != null) {
                lines.add(line);
            }
        }
        return lines;
    }

    private static List<String> unifiedDiff(List<String> lines1, List<String> lines2, String file1Path, String file2Path) throws IOException {
        List<String> diffLines = new ArrayList<>();
        DiffUtils.Diff diff = DiffUtils.diff(lines1, lines2, file1Path, file2Path);
        for (String line : diff.getUnifiedDiff()) {
            diffLines.add(line);
        }
        return diffLines;
    }

    public static void main(String[] args) {
        try {
            List<String> differences = compareFiles("path/to/file1.txt", "path/to/file2.txt");
            System.out.println("Differences: " + differences);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}