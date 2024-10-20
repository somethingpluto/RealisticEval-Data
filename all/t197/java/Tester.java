package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;
import static org.real.temp.Answer.*;
public class Tester {


    @Test
    public void testCase1() {
        assertEquals(4, josephus(7, 3));  // Standard case
    }

    @Test
    public void testCase2() {
        assertEquals(1, josephus(1, 1));  // Only one person
    }

    @Test
    public void testCase3() {
        assertEquals(3, josephus(5, 2));  // Smaller group, step 2
    }

    @Test
    public void testCase4() {
        assertEquals(3, josephus(10, 5));  // Larger group, step 5
    }

    @Test
    public void testCase5() {
        assertEquals(6, josephus(6, 1));  // Eliminate every 1st person
    }

    @Test
    public void testCase6() {
        assertEquals(6, josephus(8, 4));  // Step 4 in a group of 8
    }

    @Test
    public void testCase7() {
        assertEquals(12, josephus(12, 7));  // Larger group, arbitrary step
    }
}
