package org.real.temp;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import org.json.JSONObject;
import org.json.JSONTokener;

public class Answer {

    /**
     * Reads a JSON Lines file and returns its content as a list of dictionaries.
     *
     * @param filePath The path to the JSON Lines file.
     * @return A list of JSON objects parsed from the file.
     * @throws IOException If the specified file does not exist or there is an error reading the file.
     */
    public static List<JSONObject> readJsonl(String filePath) throws IOException {
        // Check if the file exists
        if (!new java.io.File(filePath).exists()) {
            throw new IOException("The file '" + filePath + "' does not exist.");
        }

        List<JSONObject> jsonList = new ArrayList<>();
        try (BufferedReader reader = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = reader.readLine()) != null) {
                try {
                    JSONObject jsonObject = new JSONObject(new JSONTokener(line));
                    jsonList.add(jsonObject);
                } catch (Exception e) {
                    throw new IOException("Error parsing line: " + line.trim() + " - " + e.getMessage());
                }
            }
        }

        return jsonList;
    }

    public static void main(String[] args) {
        try {
            List<JSONObject> jsonObjects = readJsonl("path/to/your/file.jsonl");
            System.out.println(jsonObjects);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}