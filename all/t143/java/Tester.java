package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;
import static org.real.temp.Answer.*;
public class Tester {

    @Test
    public void testConvertsSingleArabicNumeralsToEnglish() {
        assertEquals("1", arabicToEnglishNumbers("١"));
        assertEquals("5", arabicToEnglishNumbers("٥"));
        assertEquals("9", arabicToEnglishNumbers("٩"));
    }

    @Test
    public void testConvertsStringOfArabicNumeralsToEnglish() {
        assertEquals("0123456789", arabicToEnglishNumbers("٠١٢٣٤٥٦٧٨٩"));
    }

    @Test
    public void testHandlesStringsWithArabicAndEnglishNumeralsMixed() {
        assertEquals("012345", arabicToEnglishNumbers("٠١23٤5"));
    }

    @Test
    public void testLeavesNonNumeralCharactersUnchanged() {
        assertEquals("Hello World!", arabicToEnglishNumbers("Hello World!"));
        assertEquals("2022-2023", arabicToEnglishNumbers("2022-٢٠٢٣"));
    }

    @Test
    public void testWorksWithFullSentencesIncludingArabicNumerals() {
        assertEquals("The year is 2024!", arabicToEnglishNumbers("The year is ٢٠٢٤!"));
    }

    @Test
    public void testHandlesEmptyStringsCorrectly() {
        assertEquals("", arabicToEnglishNumbers(""));
    }

    @Test
    public void testProcessesArabicNumeralsInComplexMixedContext() {
        assertEquals("Price: 500$ and Date: 2023-12-01", 
                     arabicToEnglishNumbers("Price: ٥٠٠$ and Date: ٢٠٢٣-١٢-٠١"));
    }
}