package org.real.temp;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;

public class Answer {
    /**
     * Decodes HTML entities in a given HTML string.
     * @param htmlString The HTML string containing entities to decode.
     * @return The decoded string with HTML entities converted back to their original characters.
     */
    public static String replaceHtmlEntities(String htmlString) {
        if (htmlString == null) {
            throw new IllegalArgumentException("Input must be a string.");
        }

        // Use Jsoup to parse the string as HTML
        Document doc = Jsoup.parse(htmlString);
        
        // Return the text content, effectively decoding HTML entities
        return doc.body().text();
    }
}