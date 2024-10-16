package org.real.temp;

import java.io.UnsupportedEncodingException;
import java.net.URLEncoder;
import java.util.Map;

public class Answer {

    /**
     * Converts a map to a query string.
     *
     * @param params - The parameters to convert.
     * @return - The query string.
     */
    public static String toQueryString(Map<String, Object> params) {
        StringBuilder queryParts = new StringBuilder();

        for (Map.Entry<String, Object> entry : params.entrySet()) {
            String key = entry.getKey();
            Object value = entry.getValue();

            // Check for null values
            if (value != null) {
                try {
                    // Encode the key and value, then add to the StringBuilder
                    if (queryParts.length() > 0) {
                        queryParts.append("&");
                    }
                    queryParts.append(URLEncoder.encode(key, "UTF-8"))
                              .append("=")
                              .append(URLEncoder.encode(value.toString(), "UTF-8"));
                } catch (UnsupportedEncodingException e) {
                    // Handle the exception as needed
                    e.printStackTrace();
                }
            }
        }

        return queryParts.length() > 0 ? "?" + queryParts.toString() : "";
    }
}