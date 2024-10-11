package org.real.temp;

import java.util.*;

public class Answer {
    public static Map<String, List<String>> classifyFilesByExtension(List<String> fileNames) {
        // Create a new HashMap to store the classified files
        Map<String, List<String>> classifiedFiles = new HashMap<>();

        for(String fileName : fileNames){
            // Split the filename at the last '.' character to get the extension
            String[] parts = fileName.split("\\.");
            String extension = "";

            if(parts.length > 1){
                extension = parts[parts.length - 1];
            }

            // If the extension is not in the map yet, add it
            if(!classifiedFiles.containsKey(extension)){
                classifiedFiles.put(extension, new ArrayList<>());
            }

            // Add the filename to the list of its extension
            classifiedFiles.get(extension).add(fileName);
        }

        return classifiedFiles;
    }
}