package com.real.t170;

public class Adapted {
    /**
     * convert the HTML string to the corresponding MarkDown formatted text. HTML tags that support conversion include a, strong, code, em, p, br, u, ul, li, ol
     * @param html
     * @return
     */
    public static String convert(String html) {
        // Replace line breaks
        String markdown = html.replaceAll("(?i)<br\\s*/?>", "\n");

        // Replace paragraph tags
        markdown = markdown.replaceAll("(?i)<p>", "");
        markdown = markdown.replaceAll("(?i)</p>", "\n\n");

        // Replace strong and bold tags
        markdown = markdown.replaceAll("(?i)<strong>", "**");
        markdown = markdown.replaceAll("(?i)</strong>", "**");

        // Replace italic tags with emphasis
        markdown = markdown.replaceAll("(?i)<em>", "*");
        markdown = markdown.replaceAll("(?i)</em>", "*");

        // Replace underline (not native to markdown, commonly represented with emphasis)
        markdown = markdown.replaceAll("(?i)<u>", "*");
        markdown = markdown.replaceAll("(?i)</u>", "*");

        // Replace code tags
        markdown = markdown.replaceAll("(?i)<code>", "`");
        markdown = markdown.replaceAll("(?i)</code>", "`");

        // Replace unordered lists
        markdown = markdown.replaceAll("(?i)<ul>", "");
        markdown = markdown.replaceAll("(?i)</ul>", "");

        // Replace ordered lists
        markdown = markdown.replaceAll("(?i)<ol>", "");
        markdown = markdown.replaceAll("(?i)</ol>", "");

        // Replace list items
        markdown = markdown.replaceAll("(?i)<li>", "* ");
        markdown = markdown.replaceAll("(?i)</li>", "\n");

        // Correctly replace anchor tags in one pass
        markdown = markdown.replaceAll("(?i)<a\\s+href=\"([^\"]*)\">(.*?)</a>", "[$2]($1)");

        return markdown;
    }
}
