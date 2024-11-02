package org.real.temp;

import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class Answer {

    public static void main(String[] args) {
        String text = "Contact us at +1 555-123-4567 or (555) 555-5555.";
        System.out.println(replacePhoneNumbers(text));
    }

    /**
     * Replaces phone numbers in the given text with [PHONE_NUM].
     *
     * @param text The input text containing potential phone numbers.
     * @return The text with phone numbers replaced by [PHONE_NUM].
     */
    public static String replacePhoneNumbers(String text) {
        String phonePattern = "\\b(?:\\+\\d{1,2}\\s?)?(\\d{1,4}[-.\\s]?)?\\(?\\d{1,4}\\)?[-.\\s]?\\d{1,9}[-.\\s]?\\d{1,9}\\b"
                ;

        Pattern pattern = Pattern.compile(phonePattern);
        Matcher matcher = pattern.matcher(text);
        String replacedText = matcher.replaceAll("[PHONE_NUM]");

        return replacedText;
    }
}