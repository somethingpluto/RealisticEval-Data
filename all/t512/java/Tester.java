package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import static org.real.temp.Answer.*;
public class Tester {


    @Test
    public void testNoHoles() {
        List<Integer> holes = new ArrayList<>();
        List<Integer> expected = new ArrayList<>(Arrays.asList(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1));
        List<Integer> result = convertToRingFormat(holes);
        assertEquals(expected, result);
    }

    @Test
    public void testSingleHole() {
        List<Integer> holes = new ArrayList<>(Arrays.asList(5));
        List<Integer> expected = new ArrayList<>(Arrays.asList(1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1));
        List<Integer> result = convertToRingFormat(holes);
        assertEquals(expected, result);
    }

    @Test
    public void testMultipleHoles() {
        List<Integer> holes = new ArrayList<>(Arrays.asList(0, 2, 4, 8, 16));
        List<Integer> expected = new ArrayList<>(Arrays.asList(0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1));
        List<Integer> result = convertToRingFormat(holes);
        assertEquals(expected, result);
    }


    @Test
    public void testAllHoles() {
        List<Integer> holes = new ArrayList<>();
        for (int i = 0; i < 32; i++) {
            holes.add(i);
        }
        List<Integer> expected = new ArrayList<>(Arrays.asList(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0));
        List<Integer> result = convertToRingFormat(holes);
        assertEquals(expected, result);
    }
}