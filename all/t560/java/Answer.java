package org.real.temp;
public class Answer{
/**
 * Gets the line number in the content at the specified index.
 *
 * @param content The string content to check.
 * @param index The character index to find the line number for.
 * @return The line number corresponding to the given index.
 */
public static int getLineNumber(String content, int index) {
    if (content == null || index < 0 || index > content.length()) {
        throw new IllegalArgumentException("Invalid content or index");
    }
    return content.substring(0, index).split("\n", -1).length;
}
}

