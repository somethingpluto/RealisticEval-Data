package org.real.temp;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
import java.nio.charset.StandardCharsets;

public class Tester {

    public static Tuple<Integer, String> extractCharacterBits(byte[] byteArray, char character, String charset) {
        try {
            String decodedString = new String(byteArray, charset);
            int pos = decodedString.indexOf(character);
            if (pos != -1) {
                return new Tuple<>(pos, Integer.toBinaryString((int) decodedString.charAt(pos)).substring(8));
            }
        } catch (Exception e) {
            // Handle exception if needed
        }
        return null;
    }

    @Test
    public void testExtractChar() {
        byte[] byteArray = "Hello World".getBytes(StandardCharsets.UTF_8);
        char charToFind = 'o';
        int expectedPos = 4;
        String expectedBits = "01101111";
        Tuple<Integer, String> result = extractCharacterBits(byteArray, charToFind, StandardCharsets.UTF_8.toString());
        assertEquals(expectedPos, result.getFirst());
        assertEquals(expectedBits, result.getSecond());
    }

    @Test
    public void testCharNotFound() {
        byte[] byteArray = "Hello World".getBytes(StandardCharsets.UTF_8);
        char charToFind = 'z';
        Tuple<Integer, String> expectedResult = null;
        Tuple<Integer, String> result = extractCharacterBits(byteArray, charToFind, StandardCharsets.UTF_8.toString());
        assertEquals(expectedResult, result);
    }

    // Helper class for Tuple since Java doesn't have built-in support
    public static class Tuple<X, Y> {
        private final X first;
        private final Y second;

        public Tuple(X first, Y second) {
            this.first = first;
            this.second = second;
        }

        public X getFirst() {
            return first;
        }

        public Y getSecond() {
            return second;
        }
    }
}