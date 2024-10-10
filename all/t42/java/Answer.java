package org.real.temp;

public class Answer {

    public static String replacePhoneNumber(String text) {
        // Regular expression for matching phone numbers in various formats
        String regex = "\\b\\d{3}[-.]?\\d{3}[-.]?\\d{4}\\b";
        return text.replaceAll(regex, "[PHONE_NUM]");
    }

}