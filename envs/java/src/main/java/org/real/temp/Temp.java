package org.real.temp;

/**
 * Given a set of points and a query point, this class finds the K nearest neighbors to the query point.
 * The algorithm efficiently handles large datasets, and the output includes the coordinates of these neighbors.
 */
public class Temp {
    /**
     * Convert the HTML string to the corresponding Markdown formatted text.
     * HTML tags that support conversion include a, strong, code, em, p, br, u, ul, li, ol.
     *
     * @param html The input HTML string.
     * @return The converted Markdown formatted text.
     */
    public static String convert(String html) {
        // Replace HTML tags with Markdown equivalents
        html = html.replaceAll("(?i)<strong>(.*?)</strong>", "**$1**"); // strong
        html = html.replaceAll("(?i)<em>(.*?)</em>", "*$1*"); // em
        html = html.replaceAll("(?i)<u>(.*?)</u>", "_$1_"); // underline (u)
        html = html.replaceAll("(?i)<code>(.*?)</code>", "`$1`"); // code
        html = html.replaceAll("(?i)<p>(.*?)</p>", "$1\n\n"); // paragraphs
        html = html.replaceAll("(?i)<br\\s*/?>", "\n"); // line breaks (br)

        // Handle lists
        html = html.replaceAll("(?i)<ul>(.*?)</ul>", "<ul>$1</ul>");
        html = html.replaceAll("(?i)<ol>(.*?)</ol>", "<ol>$1</ol>");
        html = html.replaceAll("(?i)<li>(.*?)</li>", "* $1\n"); // unordered list items

        // Replace <a> tag with Markdown links
        html = html.replaceAll("(?i)<a href=\"(.*?)\">(.*?)</a>", "[$2]($1)");

        // Remove any remaining HTML tags
        html = html.replaceAll("<[^>]+>", "");

        return html.trim();
    }
}
