package org.real.temp;

import org.junit.Test;

import java.util.List;

import static org.junit.Assert.assertEquals;

public class Tester {

    @Test
    public void testCase3() {
        // Test with a string that has no uppercase letters
        List<String> result = Answer.removePartsOfStrings("abcdefg");
        assertEquals("[abcdefg]", result.toString());
    }

    @Test
    public void testCase4() {
        // Test with a string that has no lowercase letters
        List<String> result = Answer.removePartsOfStrings("ABCDEFG");
        assertEquals("[ABCDEFG]", result.toString());
    }

    @Test
    public void testCase5() {
        // Test with a string that has mixed cases
        List<String> result = Answer.removePartsOfStrings("1234AbCde5678");
        assertEquals("[AbCde5678]", result.toString());
    }

    @Test
    public void testCase6() {
        // Test with an empty string
        List<String> result = Answer.removePartsOfStrings("");
        assertEquals("[]", result.toString());
    }

    @Test
    public void testCase7() {
        // Test with a string that has only one uppercase letter
        List<String> result = Answer.removePartsOfStrings("X");
        assertEquals("[X]", result.toString());
    }

    @Test
    public void testCase8() {
        // Test with a string that has only one lowercase letter
        List<String> result = Answer.removePartsOfStrings("y");
        assertEquals("[y]", result.toString());
    }
}