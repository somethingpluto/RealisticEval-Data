package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.*;
import java.util.Arrays;

public class Tester {

    @Test
    public void testCorrectlySeparatesMIDINotes() {
        int[] midiNotes = {60, 61, 62};  // C4, C#4, D4
        NoteSeparation expected = new NoteSeparation(Arrays.asList(5, 5, 5), Arrays.asList(0, 1, 2));  // Octaves and root notes
        assertEquals(expected, separateOctaveAndRoot(midiNotes));
    }

    @Test
    public void testHandlesSingleMIDIInput() {
        int[] midiNotes = {24};  // C1
        NoteSeparation expected = new NoteSeparation(Arrays.asList(2), Arrays.asList(0));  // 2nd octave, C note
        assertEquals(expected, separateOctaveAndRoot(midiNotes));
    }

    @Test
    public void testReturnsEmptyArraysForEmptyInput() {
        int[] midiNotes = {};  // Empty input
        NoteSeparation expected = new NoteSeparation(Arrays.asList(), Arrays.asList());
        assertEquals(expected, separateOctaveAndRoot(midiNotes));
    }

    @Test(expected = IllegalArgumentException.class)
    public void testThrowsErrorForInvalidInputTypes() {
        // Invalid input as string
        separateOctaveAndRoot(null);  // Assuming null is treated as invalid input

        // Invalid input as array with non-integers (e.g., float)
        separateOctaveAndRoot(new int[]{(int) 3.14}); // Directly throws error in Java, so no need for a catch block
    }

    @Test
    public void testHandlesMIDINotesFromDifferentOctaves() {
        int[] midiNotes = {12, 25, 37};  // C1, C#2, D#3
        NoteSeparation expected = new NoteSeparation(Arrays.asList(1, 2, 3), Arrays.asList(0, 1, 1));  // Octaves and root notes
        assertEquals(expected, separateOctaveAndRoot(midiNotes));
    }

    // Assuming the separateOctaveAndRoot method is already defined elsewhere in the Tester class or another class
    public NoteSeparation separateOctaveAndRoot(int[] midiNotes) {
        // Method implementation goes here
        return null;  // Placeholder
    }

    // Assuming NoteSeparation class has proper equals and hashCode methods implemented
}