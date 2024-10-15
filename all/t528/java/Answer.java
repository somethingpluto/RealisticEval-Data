package org.real.temp;

import java.io.File;
import java.util.ArrayList;
import java.util.List;

public class Answer {

    /**
     * Recursively searches for Markdown files in the specified directory.
     *
     * @param dir - The directory path to search in.
     * @return - A list of paths to Markdown files.
     */
    public static List<String> findMarkdownFiles(String dir) {
        List<String> markdownFiles = new ArrayList<>();
        File directory = new File(dir);

        // Check if the directory exists and is indeed a directory
        if (directory.exists() && directory.isDirectory()) {
            File[] files = directory.listFiles();

            if (files != null) {
                for (File file : files) {
                    // If it's a directory, recurse into it
                    if (file.isDirectory()) {
                        markdownFiles.addAll(findMarkdownFiles(file.getAbsolutePath()));
                    }
                    // If it's a Markdown file, add it to the list
                    else if (file.getName().endsWith(".md")) {
                        markdownFiles.add(file.getAbsolutePath());
                    }
                }
            }
        }
        
        return markdownFiles;
    }

    public static void main(String[] args) {
        String directoryPath = "path/to/your/directory"; // Change to your directory path
        List<String> markdownFiles = findMarkdownFiles(directoryPath);
        markdownFiles.forEach(System.out::println);
    }
}