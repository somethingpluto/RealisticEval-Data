package org.real.temp;


import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

public class Answer {

    public static Map<String, Object> parseJsonFile(String filePath) {
        Map<String, Object> jsonMap = new HashMap<>();

        try (BufferedReader reader = new BufferedReader(new FileReader(filePath))) {
            StringBuilder jsonStringBuilder = new StringBuilder();
            String line;

            // Read the JSON file line by line
            while ((line = reader.readLine()) != null) {
                jsonStringBuilder.append(line);
            }

            // Convert the JSON string to a JSONObject
            JSONObject jsonObject = new JSONObject(jsonStringBuilder.toString());

            // Convert the JSONObject to a Map
            jsonMap = jsonToMap(jsonObject);

        } catch (IOException e) {
            e.printStackTrace(); // Handle file reading exceptions
        }

        return jsonMap;
    }

    private static Map<String, Object> jsonToMap(JSONObject jsonObject) {
        Map<String, Object> map = new HashMap<>();

        // Iterate through the keys of the JSONObject
        for (String key : jsonObject.keySet()) {
            Object value = jsonObject.get(key);
            // If the value is a JSONObject, convert it to a Map recursively
            if (value instanceof JSONObject) {
                map.put(key, jsonToMap((JSONObject) value));
            } else {
                map.put(key, value);
            }
        }

        return map;
    }
}
