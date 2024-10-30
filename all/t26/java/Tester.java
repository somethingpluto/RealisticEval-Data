package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;
import static org.real.temp.Answer.*;
public class Tester {

    /**
     * Tests conversion of basic separators.
     */
    @Test
    public void testBasicSeparators() {
        assertEquals("Failed to convert basic separators.",
                     "apple,banana,orange,mango",
                     convertToCommaSeparated("apple;banana*orange/mango"));
    }

    /**
     * Tests conversion of mixed separators in a string.
     */
    @Test
    public void testMixedSeparators() {
        assertEquals("Failed to convert mixed separators in a string.",
                     "grapes,lemon,melon,kiwi,litchi",
                     convertToCommaSeparated("grapes;lemon/melon*kiwi;litchi"));
    }

    /**
     * Tests conversion of mixed separators in another string.
     */
    @Test
    public void testMixedSeparators2() {
        assertEquals("Failed to convert mixed separators in a string.",
                     "grapes,lemon,melon,kiwi,litchi",
                     convertToCommaSeparated("grapes/lemon/melon*kiwi*litchi"));
    }

    /**
     * Tests the case where no separators are present.
     */
    @Test
    public void testNoSeparators() {
        assertEquals("Failed when no separators are present.",
                     "watermelon",
                     convertToCommaSeparated("watermelon"));
    }
}