package org.real.temp;

import junit.framework.TestCase;
import java.util.regex.Pattern;
import java.util.regex.Matcher;
import java.util.ArrayList;
import java.util.List;

public class Tester extends TestCase {

    // Assuming you have a method that needs testing, for example, findPlaceholders
    public void testFindPlaceholders() {
        String inputText = "This is a sample text with placeholders like {{ name }}, {{ age }}, and {{ address }}.";
        List<String> expectedPlaceholders = new ArrayList<>();
        expectedPlaceholders.add("{{ name }}");
        expectedPlaceholders.add("{{ age }}");
        expectedPlaceholders.add("{{ address }}");

        List<String> actualPlaceholders = findPlaceholders(inputText);

        assertEquals(expectedPlaceholders.size(), actualPlaceholders.size());
        for (String expected : expectedPlaceholders) {
            assertTrue(actualPlaceholders.contains(expected));
        }
    }

    private List<String> findPlaceholders(String text) {
        Pattern pattern = Pattern.compile("\\{\\{\\s*([a-zA-Z0-9_]+)\\s*\\}\\}");
        Matcher matcher = pattern.matcher(text);
        List<String> placeholders = new ArrayList<>();

        while (matcher.find()) {
            placeholders.add(matcher.group(1));
        }

        return placeholders;
    }
}