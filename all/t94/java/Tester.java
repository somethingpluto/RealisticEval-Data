package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.*;

import java.util.Arrays;
import java.util.List;

public class Tester {

    @Test
    public void shouldReturn12NotesInTheCircle() {
        List<String> result = createCircleOfFifths("C");
        assertEquals(12, result.size());
    }

    @Test
    public void shouldStartWithTheGivenStartingNote() {
        String startingNote = "G";
        List<String> result = createCircleOfFifths(startingNote);
        assertEquals(startingNote, result.get(0));
    }

    @Test
    public void shouldCorrectlyGenerateTheCircleOfFifthsStartingFromC() {
        List<String> result = createCircleOfFifths("C");
        List<String> expectedCircle = Arrays.asList("C", "G", "D", "A", "E", "B", "F#", "C#", "G#", "D#", "A#", "E#");
        assertEquals(expectedCircle, result);
    }

    @Test
    public void shouldCorrectlyGenerateTheCircleOfFifthsStartingFromG() {
        List<String> result = createCircleOfFifths("G");
        List<String> expectedCircle = Arrays.asList("G", "D", "A", "E", "B", "F#", "C#", "G#", "D#", "A#", "E#", "B#");
        assertEquals(expectedCircle, result);
    }

    @Test
    public void shouldCorrectlyGenerateTheCircleOfFifthsStartingFromF() {
        List<String> result = createCircleOfFifths("F");
        List<String> expectedCircle = Arrays.asList("F", "C", "G", "D", "A", "E", "B", "F#", "C#", "G#", "D#", "A#");
        assertEquals(expectedCircle, result);
    }

    // Stub for createCircleOfFifths method
    public static List<String> createCircleOfFifths(String startingNote) {
        // Implement this method based on your logic
        return null; // Placeholder return statement
    }
}