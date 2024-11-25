package org.real.temp;


public class Answer {
    // Example method to be tested (this would typically be in your class)
    public static String safeFormat(String template, String... values) {
        if (values.length == 0) {
            return template;
        }

        for (int i = 0; i < values.length; i++) {
            template = template.replace("{" + "name" + "}", values[i]); // Sample placeholder format
        }
        return template;
    }
}
