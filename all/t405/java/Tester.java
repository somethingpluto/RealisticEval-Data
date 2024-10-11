package org.real.temp;

import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;

public class Tester {

    @Test
    public void testRemovePartsOfString() {
        // Test case 1
        assertEquals("AbCde5678", removePartsOfStrings("1234AbCde5678"));

        // Test case 2
        assertEquals("HelloWorld", removePartsOfStrings("HelloWorld"));

        // Test case 3
        assertEquals("JavaIsFun", removePartsOfStrings("JavaIsFun"));

        // Test case 4
        assertEquals("", removePartsOfStrings("1234567890"));

        // Test case 5
        assertEquals("", removePartsOfStrings("!@#$%^&*()_+"));

        // Test case 6
        assertEquals("ABCD", removePartsOfStrings("ABCD"));
    }

    private String removePartsOfStrings(String... strings) {
        if (strings == null || strings.length == 0) {
            return "";
        }

        String input = strings[0];
        int startIndex = -1;
        int endIndex = -1;

        for (int i = 0; i < input.length(); i++) {
            char c = input.charAt(i);
            if (Character.isUpperCase(c)) {
                startIndex = i;
            } else if (Character.isLowerCase(c)) {
                endIndex = i;
                break;
            }
        }

        if (startIndex == -1 || endIndex == -1) {
            return input;
        }

        return input.substring(startIndex, endIndex + 1);
    }
}