package org.real.temp;
import java.net.URI;
import java.net.URISyntaxException;
import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;
import java.util.LinkedHashMap;
import java.util.Map;

public class Answer {

    /**
     * Removes the specified parameter from the URL query string.
     *
     * @param url The URL from which to remove the parameter.
     * @param key The key of the parameter to remove.
     * @return The modified URL with the specified parameter removed.
     * @throws URISyntaxException If the URL is malformed.
     */
    public static String removeQueryParam(String url, String key) throws URISyntaxException {
        URI uri = new URI(url);
        String query = uri.getQuery();
        Map<String, String> params = new LinkedHashMap<>();

        if (query != null) {
            String[] pairs = query.split("&");
            for (String pair : pairs) {
                int idx = pair.indexOf("=");
                String paramKey = URLDecoder.decode(pair.substring(0, idx), StandardCharsets.UTF_8);
                String paramValue = idx > 0 ? URLDecoder.decode(pair.substring(idx + 1), StandardCharsets.UTF_8) : "";
                if (!paramKey.equals(key)) {
                    params.put(paramKey, paramValue);
                }
            }
        }

        StringBuilder newQuery = new StringBuilder();
        for (Map.Entry<String, String> entry : params.entrySet()) {
            if (newQuery.length() > 0) {
                newQuery.append("&");
            }
            newQuery.append(URLEncoder.encode(entry.getKey(), StandardCharsets.UTF_8));
            newQuery.append("=");
            newQuery.append(URLEncoder.encode(entry.getValue(), StandardCharsets.UTF_8));
        }

        return new URI(uri.getScheme(), uri.getAuthority(), uri.getPath(), newQuery.toString(), uri.getFragment()).toString();
    }

    public static void main(String[] args) {
        try {
            String modifiedUrl = removeQueryParam("http://example.com?param1=value1&param2=value2", "param1");
            System.out.println(modifiedUrl);
        } catch (URISyntaxException e) {
            e.printStackTrace();
        }
    }
}