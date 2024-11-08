package org.real.temp;

import java.net.URL;
import java.net.URLDecoder;
import java.nio.charset.StandardCharsets;
import java.util.HashMap;
import java.util.Map;

public class Answer {

    /**
     * Extract the file ID from the given URL query args.
     *
     * @param url - The URL from which the file ID is to be extracted.
     * @return - The extracted file ID if present, otherwise null if the URL does not conform to the expected format.
     */
    public static String getFileIdFromUrl(String url) {
        try {
            URL urlObject = new URL(url);
            String query = urlObject.getQuery();
            Map<String, String> queryPairs = new HashMap<>();

            for (String pair : query.split("&")) {
                int idx = pair.indexOf("=");
                queryPairs.put(URLDecoder.decode(pair.substring(0, idx), StandardCharsets.UTF_8), 
                               URLDecoder.decode(pair.substring(idx + 1), StandardCharsets.UTF_8));
            }

            return queryPairs.get("fileId"); // Return the decoded file ID if found
        } catch (Exception e) {
            System.err.println("Invalid URL: " + e);
            return null; // Return null if the URL is invalid or an error occurs.
        }
    }
}