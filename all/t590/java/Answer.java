package org.real.temp;

import java.util.HashMap;
import java.util.Map;

public class Answer {

    public static Map<String, String> parseHttpRequestLine(String response) {
        // Initialize the result map
        Map<String, String> result = new HashMap<>();

        // Step 1: Find the position of the first line of the response (request line)
        int endOfFirstLine = response.indexOf("\r\n");

        if (endOfFirstLine == -1) {
            // If no valid line break is found, return an empty map
            return result;
        }

        // Step 2: Extract the first line (the request line)
        String requestLine = response.substring(0, endOfFirstLine);

        // Step 3: Split the request line into method, URL, and version
        String[] parts = requestLine.split(" ");
        
        if (parts.length >= 3) {
            // Parse method (e.g., GET, POST)
            String method = parts[0];

            // Parse URL (e.g., /index.html)
            String url = parts[1];

            // Parse HTTP version (e.g., HTTP/1.1)
            String httpVersion = parts[2];

            // Step 4: Store the parsed information in the result map
            result.put("method", method);
            result.put("url", url);
            result.put("http_version", httpVersion);
        }

        // Step 5: Return the result map
        return result;
    }
}