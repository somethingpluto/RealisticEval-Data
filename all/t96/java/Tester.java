package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class Tester {

    @Test
    public void testInsertClefDefault() {
        String abc = "X:1\nT:Test Tune\nK:C\nC D E F|G A B c|\n";
        String result = AbcModifier.changedClef(abc, null);
        String expected = "X:1\nT:Test Tune\nK:C clef=bass\nC D E F|G A B c|\n";
        assertEquals(expected, result);
    }

    @Test
    public void testInsertClefSpecific() {
        String abc = "X:1\nT:Test Tune\nK:C\nC D E F|G A B c|\n";
        String result = AbcModifier.changedClef(abc, "treble");
        String expected = "X:1\nT:Test Tune\nK:C clef=treble\nC D E F|G A B c|\n";
        assertEquals(expected, result);
    }

    @Test
    public void testNoNewlineAfterKeySignature() {
        String abc = "X:1\nT:Test Tune\nK:C";
        String result = AbcModifier.changedClef(abc, "alto");
        String expected = "X:1\nT:Test Tune\nK:C clef=alto";
        assertEquals(expected, result);
    }

    @Test
    public void testNoKeySignatureFound() {
        String abc = "X:1\nT:Test Tune\nC D E F|G A B c|\n";
        String result = AbcModifier.changedClef(abc, "tenor");
        assertEquals(abc, result); // Expect the original string to be returned unchanged
    }

    @Test
    public void testMultipleKeySignatures() {
        String abc = "X:1\nT:Test Tune\nK:G\nG A B c|\nK:D\nD E F# G|\n";
        String result = AbcModifier.changedClef(abc, "baritone");
        String expected = "X:1\nT:Test Tune\nK:G clef=baritone\nG A B c|\nK:D\nD E F# G|\n";
        assertEquals(expected, result);
    }
}