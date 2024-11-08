package org.real.temp;

import static org.junit.Assert.assertEquals;
import org.junit.Test;
import static org.real.temp.Answer.*;
public class Tester {

    @Test
    public void testCountLetters_HelloWorld() {
        assertEquals(10, countLetters("Hello, World!"));
    }

    @Test
    public void testCountLetters_NoLetters() {
        assertEquals(0, countLetters("12345"));
    }

    @Test
    public void testCountLetters_ABC123XYZ() {
        assertEquals(6, countLetters("abc 123 xyz!"));
    }

    @Test
    public void testCountLetters_EmptyString() {
        assertEquals(0, countLetters(""));
    }

    @Test
    public void testCountLetters_MixedCharacters() {
        assertEquals(3, countLetters("A1B2C3!@#"));
    }

    @Test
    public void testCountLetters_MixedCase() {
        assertEquals(5, countLetters("AbCdE"));
    }

    @Test
    public void testCountLetters_SpecialCharacters() {
        assertEquals(5, countLetters("Hello@2024!"));
    }
}