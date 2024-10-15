package org.real.temp;

public class Answer {

    /**
     * Compresses an HTML string by removing unnecessary whitespace,
     * including newlines, tabs, and extra spaces,
     * while preserving the structure of the HTML.
     * 
     * @param html The input HTML string to be compressed.
     * @return The compressed HTML string with reduced whitespace.
     */
    public static String compressHtml(String html) {
        if (html == null) {
            return null;
        }

        // Remove all newline and tab characters from the string
        html = html.replaceAll("[\\r\\n\\t]+", ""); // Removes newlines and tabs
        
        // Replace multiple consecutive spaces with a single space
        html = html.replaceAll(" {2,}", " "); // Replaces multiple spaces with a single space
        
        // Remove spaces between HTML tags (e.g., transforming "> <" into "><")
        html = html.replaceAll("> <", "><"); // Removes spaces between HTML tags
        
        // Trim any leading and trailing whitespace from the final string
        return html.trim(); // Trims whitespace from the start and end of the string
    }

    public static void main(String[] args) {
        String htmlInput = "<div>   <p>   Hello,    World!  </p>  </div>";
        String compressedHtml = compressHtml(htmlInput);
        System.out.println(compressedHtml);
    }
}