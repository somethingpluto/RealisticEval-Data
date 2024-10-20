package org.real.temp;

import org.json.JSONArray;
import org.json.JSONObject;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

public class Answer {
    
    public List<JSONObject> concatenateJsonArrays(String directory) {
        List<JSONObject> combinedData = new ArrayList<>();

        File dir = new File(directory);
        // List all files in the directory
        File[] files = dir.listFiles((d, name) -> name.endsWith(".json"));

        if (files != null) {
            for (File file : files) {
                try {
                    // Read the JSON file as a string
                    String content = new String(Files.readAllBytes(Paths.get(file.getPath())));
                    // Parse the JSON content
                    Object data = new JSONObject(content);

                    // Check if the data is a JSONArray
                    if (data instanceof JSONArray) {
                        JSONArray jsonArray = (JSONArray) data;
                        for (int i = 0; i < jsonArray.length(); i++) {
                            combinedData.add(jsonArray.getJSONObject(i));
                        }
                    } else {
                        System.out.println("Warning: " + file.getName() + " does not contain a root-level array.");
                    }
                } catch (FileNotFoundException e) {
                    System.err.println("File not found: " + file.getName());
                } catch (IOException e) {
                    System.err.println("Error reading file: " + file.getName());
                } catch (Exception e) {
                    System.err.println("Error processing file: " + file.getName() + " - " + e.getMessage());
                }
            }
        }

        return combinedData;
    }
}
