package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;
import static org.real.temp.Answer.*;
public class Tester {

    @Test
    public void testCountDashes_NoDashes() {
        int result = countDashes("hello world");
        assertEquals(0, result); // 'hello world' contains no dashes
    }

    @Test
    public void testCountDashes_OneDash() {
        int result = countDashes("hello-world");
        assertEquals(1, result); // 'hello-world' contains one dash
    }

    @Test
    public void testCountDashes_MultipleDashes() {
        int result = countDashes("a-b-c-d-e");
        assertEquals(4, result); // 'a-b-c-d-e' contains four dashes
    }

    @Test
    public void testCountDashes_DashesAtEnds() {
        int result = countDashes("-start-end-");
        assertEquals(3, result); // '-start-end-' contains three dashes
    }

    @Test
    public void testCountDashes_EmptyString() {
        int result = countDashes("");
        assertEquals(0, result); // An empty string contains no dashes
    }
}