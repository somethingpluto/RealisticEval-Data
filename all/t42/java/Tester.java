package org.real.temp;

import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;

public class Tester {

    @Test
    public void testReplacePhoneNumbers() {
        // Test data and expected results
        String input1 = "Call me at 123-456-7890.";
        String expectedOutput1 = "Call me at [PHONE_NUM].";

        String input2 = "Reach out to us at +1 123.456.7890 or 123 456 7890.";
        String expectedOutput2 = "Reach out to us at [PHONE_NUM] or [PHONE_NUM].";

        String input3 = "No phone numbers here!";
        String expectedOutput3 = "No phone numbers here!";

        // Perform the test
        assertEquals(expectedOutput1, replace_phone_numbers(input1));
        assertEquals(expectedOutput2, replace_phone_numbers(input2));
        assertEquals(expectedOutput3, replace_phone_numbers(input3));
    }

    /**
     * Replace all phones(phone formats in many) in the string with the string [PHONE_NUM].
     *
     * @param text The input string that may contain phone numbers.
     * @return The modified string with phone numbers replaced by '[PHONE_NUM]'.
     */
    private String replace_phone_numbers(String text) {
        // Implement the logic to replace phone numbers here
        return text.replaceAll("\\b\\d{3}[ -.]?\\d{3}[ -.]?\\d{4}\\b", "[PHONE_NUM]");
    }
}