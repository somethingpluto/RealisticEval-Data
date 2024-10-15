package org.real.temp;

import java.io.FileWriter;
import java.io.IOException;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;

public class Answer {

    /**
     * Converts the data object to JSON format and saves it to the specified file path.
     * @param data - The data object to be converted to JSON.
     * @param outputFilePath - The file path where the JSON will be saved.
     */
    public static void saveAsJSON(Object data, String outputFilePath) {
        Gson gson = new GsonBuilder().setPrettyPrinting().create();
        String jsonData = gson.toJson(data);
        
        try (FileWriter fileWriter = new FileWriter(outputFilePath)) {
            fileWriter.write(jsonData);
            System.out.println("Data successfully saved to " + outputFilePath);
        } catch (IOException e) {
            System.err.println("Error saving data to file: " + e.getMessage());
        }
    }
}