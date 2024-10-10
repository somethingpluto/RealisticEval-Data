package org.real.temp;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import com.fasterxml.jackson.databind.ObjectMapper;

public class Answer {

    public static List<Map<String, Object>> extractParseDictionaries(String filePath) throws IOException {
        List<Map<String, Object>> dictionaries = new ArrayList<>();
        ObjectMapper mapper = new ObjectMapper();
        
        try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = br.readLine()) != null) {
                if (line.trim().startsWith("{") && line.trim().endsWith("}")) {
                    Map<String, Object> dict = mapper.readValue(line, Map.class);
                    dictionaries.add(dict);
                }
            }
        }
        return dictionaries;
    }

}