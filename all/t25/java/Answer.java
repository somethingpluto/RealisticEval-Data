package org.real.temp;

import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Answer {

    public static void classifyJsonObjectsByPid(String sourceFile, List<String> pidList, String matchFile, String mismatchFile) {
        ObjectMapper objectMapper = new ObjectMapper();
        
        try {
            // Load JSON objects from the source file
            List<JsonObject> data = objectMapper.readValue(new File(sourceFile), new TypeReference<List<JsonObject>>() {});
            
            // Initialize lists for matches and mismatches
            List<JsonObject> matches = new ArrayList<>();
            List<JsonObject> mismatches = new ArrayList<>();

            // Classify each object based on 'pid' presence in 'pidList'
            for (JsonObject obj : data) {
                if (pidList.contains(obj.getPid())) {
                    matches.add(obj);
                } else {
                    mismatches.add(obj);
                }
            }

            // Save the matches to a new JSON file
            objectMapper.writerWithDefaultPrettyPrinter().writeValue(new File(matchFile), matches);

            // Save the mismatches to another JSON file
            objectMapper.writerWithDefaultPrettyPrinter().writeValue(new File(mismatchFile), mismatches);

            System.out.println("Classification complete. Data saved to respective files.");
        } catch (IOException e) {
            System.err.println("An error occurred: " + e.getMessage());
        }
    }

    public static class JsonObject {
        private String pid; // Assuming 'pid' is a String, modify if necessary

        // Getter for 'pid'
        public String getPid() {
            return pid;
        }

        // Setter for 'pid'
        public void setPid(String pid) {
            this.pid = pid;
        }
    }

    public static void main(String[] args) {
        // Example usage
        List<String> pidList = List.of("pid1", "pid2", "pid3");
        classifyJsonObjectsByPid("source.json", pidList, "matches.json", "mismatches.json");
    }
}
