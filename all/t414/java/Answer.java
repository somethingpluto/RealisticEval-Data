package org.real.temp;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Answer {
    public List<Map<String, String>> extractBibInfo(String bibFile) throws IOException {
        List<Map<String, String>> results = new ArrayList<>();
        
        try (BufferedReader br = new BufferedReader(new FileReader(bibFile))) {
            StringBuilder sb = new StringBuilder();
            String line;
            
            while ((line = br.readLine()) != null) {
                if (!line.trim().startsWith("@")) {
                    sb.append(line).append("\n");
                } else {
                    Map<String, String> infoMap = parseEntry(sb.toString());
                    if (infoMap != null) {
                        results.add(infoMap);
                    }
                    sb.setLength(0); // clear stringbuilder
                    sb.append(line).append("\n"); // start new entry
                }
            }

            // add last entry if there is one
            if (sb.length() > 0) {
                Map<String, String> infoMap = parseEntry(sb.toString());
                if (infoMap != null) {
                    results.add(infoMap);
                }
            }
        }

        return results;
    }

    private Map<String, String> parseEntry(String entry) {
        Map<String, String> infoMap = new HashMap<>();

        String[] parts = entry.split(",");
        for (String part : parts) {
            part = part.trim();
            if (part.startsWith("author") || part.startsWith("title") || part.startsWith("year")) {
                String key = part.substring(0, part.indexOf("=")).trim();
                String value = part.substring(part.indexOf("=") + 1, part.indexOf(",")).trim();
                value = value.replace("{", "").replace("}", "").replace("\"", ""); // clean up value
                infoMap.put(key, value);
            }
        }

        return !infoMap.isEmpty() ? infoMap : null;
    }
}