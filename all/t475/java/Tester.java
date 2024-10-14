package org.real.temp;

import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;

public class Tester {

    /**
     * Safely formats a template string by replacing placeholders with corresponding values
     * from the provided keyword arguments. If a placeholder does not have a corresponding
     * value in kwargs, it remains unchanged.
     *
     * @param template The string template containing placeholders in the form {key}.
     * @param args Keyword arguments that map keys to their replacement values.
     * @return The formatted string with placeholders replaced by values.
     */
    public String safeFormat(String template, Object... args) {
        for (Object arg : args) {
            if (arg instanceof String && ((String) arg).startsWith("{") && ((String) arg).endsWith("}")) {
                String key = ((String) arg).substring(1, ((String) arg).length() - 1);
                int index = template.indexOf(arg);
                while (index != -1) {
                    if (index + arg.length() < template.length() && Character.isLetterOrDigit(template.charAt(index + arg.length()))) {
                        // Skip if the next character is a letter or digit to avoid partial matches
                        index = template.indexOf(arg, index + arg.length());
                    } else {
                        template = template.substring(0, index) + args[index / 2] + template.substring(index + arg.length());
                        index += args[index / 2].toString().length();
                    }
                }
            }
        }
        return template;
    }

    @Test
    public void testSafeFormat() {
        assertEquals("Hello, John!", safeFormat("Hello, {name}!", "John"));
        assertEquals("The answer is {answer}.", safeFormat("The answer is {answer}.", "42"));
        assertEquals("No replacements here.", safeFormat("No replacements here."));
        assertEquals("Keep {unchanged} unchanged.", safeFormat("Keep {unchanged} unchanged."));
        assertEquals("Replace {first}, keep {second}.", safeFormat("Replace {first}, keep {second}.", "first"));
    }
}
