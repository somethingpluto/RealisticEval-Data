package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;
import static org.real.temp.Answer.*;
public class Tester {

    @Test
    public void testCountNumbers_MultipleNumbers() {
        int result = countNumbers("There are 123 numbers in this string.");
        assertEquals(3, result); // '123' contains three numeric characters
    }

    @Test
    public void testCountNumbers_NoNumbers() {
        int result = countNumbers("No numbers here!");
        assertEquals(0, result); // No numeric characters in 'No numbers here!'
    }

    @Test
    public void testCountNumbers_MixedCharacters() {
        int result = countNumbers("Room 101 and Room 102");
        assertEquals(6, result); // '101' and '102' together contain six numeric characters
    }

    @Test
    public void testCountNumbers_OnlyNumbers() {
        int result = countNumbers("1234567890");
        assertEquals(10, result); // '1234567890' contains ten numeric characters
    }

    @Test
    public void testCountNumbers_EmptyString() {
        int result = countNumbers("");
        assertEquals(0, result); // An empty string contains no numeric characters
    }
}