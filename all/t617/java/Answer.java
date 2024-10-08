package org.real.temp;

import org.json.JSONObject;
import org.json.JSONTokener;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

public class Answer {
    /**
     * Parses a JSON file and stores its contents in a Map.
     *
     * This function reads a JSON file from the specified file path, parses the JSON data, and stores
     * each key-value pair from the JSON object into a HashMap. The function uses the org.json library
     * to handle JSON parsing. It supports basic JSON objects consisting of key-value pairs.
     *
     * @param filePath the path to the JSON file to be parsed. The file must exist and contain valid JSON.
     *                 The path should be a fully qualified path or relative to the current working directory.
     * @return a Map<String, Object> containing the key-value pairs parsed from the JSON file. If the JSON
     *         file is empty or contains only simple key-value pairs without nested structures, the resulting
     *         Map will be correspondingly simple. The function returns an empty Map if the file is empty.
     * @throws FileNotFoundException if the specified file does not exist or cannot be opened. This exception
     *         is caught within the function and logged to the standard output, but it might be more appropriate
     *         in a real-world application to rethrow it or handle it in a way that informs the user more effectively.
     *
     * Example usage:
     * Map<String, Object> jsonData = parseJsonFile("data.json");
     * for (Map.Entry<String, Object> entry : jsonData.entrySet()) {
     *     System.out.println(entry.getKey() + ": " + entry.getValue());
     * }
     */
    public static Map<String, Object> parseJsonFile(String filePath) {
        Map<String, Object> resultMap = new HashMap<>();
        try {
            FileInputStream fileInputStream = new FileInputStream(filePath);
            JSONTokener tokener = new JSONTokener(fileInputStream);
            JSONObject jsonObject = new JSONObject(tokener);

            Iterator<String> keys = jsonObject.keys();

            while (keys.hasNext()) {
                String key = keys.next();
                Object value = jsonObject.get(key);
                resultMap.put(key, value);
            }
        } catch (FileNotFoundException e) {
            System.out.println("File not found: " + filePath);
            e.printStackTrace();
        }

        return resultMap;
    }

    public static void main(String[] args) {
        String filePath = "path_to_your_json_file.json";
        Map<String, Object> data = parseJsonFile(filePath);
        System.out.println(data);
    }
}
