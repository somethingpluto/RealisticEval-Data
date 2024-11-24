package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;
import static org.real.temp.Answer.*;
/**
 * Test class for the convertToShortFormat method.
 */
public class Tester {

    /**
     * Tests a standard input with mixed characters.
     */
    @Test
    public void testBasicCase() {
        assertEquals("fpgbc", convertToShortFormat("f1_p1_g1_b1_c1"));
    }

    /**
     * Tests input with multiple segments.
     */
    @Test
    public void testMultipleSegments() {
        assertEquals("abc", convertToShortFormat("a2_b3_c4"));
    }

    /**
     * Tests input with non-alphanumeric characters.
     */
    @Test
    public void testNonAlphaNumeric() {
        assertEquals("hwt", convertToShortFormat("hello_world_test"));
    }

    /**
     * Tests a single segment input.
     */
    @Test
    public void testSingleSegment() {
        assertEquals("s", convertToShortFormat("single"));
    }
    
}