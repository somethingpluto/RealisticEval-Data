package org.real.temp;

import java.io.File;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Answer {

    /**
     * Find the common columns of all CSV files in a directory and return these column names as a list.
     *
     * @param directory the directory path
     * @return a list containing the common column names
     */
    public static List<String> findCommonColumns(String directory) {
        File dir = new File(directory);
        if (!dir.isDirectory()) {
            throw new IllegalArgumentException("The provided path is not a directory.");
        }

        Set<String> commonColumns = null;
        boolean firstFile = true;

        for (File file : dir.listFiles((d, name) -> name.endsWith(".csv"))) {
            if (file.isFile()) {
                try (BufferedReader br = new BufferedReader(new FileReader(file))) {
                    String line = br.readLine();
                    if (line != null) {
                        String[] columns = line.split(",");
                        Set<String> currentColumns = new HashSet<>();
                        for (String column : columns) {
                            currentColumns.add(column.trim());
                        }
                        if (firstFile) {
                            commonColumns = new HashSet<>(currentColumns);
                            firstFile = false;
                        } else {
                            commonColumns.retainAll(currentColumns);
                        }
                    }
                } catch (IOException e) {
                    System.err.println("Error reading file " + file.getName() + ": " + e.getMessage());
                }
            }
        }

        if (commonColumns == null || commonColumns.isEmpty()) {
            return new ArrayList<>();
        }

        return new ArrayList<>(commonColumns);
    }

    public static void main(String[] args) {
        // Example usage
        String directoryPath = "/path/to/your/csv/files";
        List<String> commonColumns = findCommonColumns(directoryPath);
        System.out.println("Common Columns: " + commonColumns);
    }
}