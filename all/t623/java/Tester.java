package org.real.temp;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
import java.awt.Color;

public class Tester {

    @Test
    public void testToRGBCode_White() {
        Color color = new Color(255, 255, 255); // White
        String expected = "#FFFFFF"; // Expected RGB Code
        String result = Answer.toRGBCode(color);
        assertEquals(expected, result);
    }

    @Test
    public void testToRGBCode_Black() {
        Color color = new Color(0, 0, 0); // Black
        String expected = "#000000"; // Expected RGB Code
        String result = Answer.toRGBCode(color);
        assertEquals(expected, result);
    }

    @Test
    public void testToRGBCode_Red() {
        Color color = new Color(255, 0, 0); // Red
        String expected = "#FF0000"; // Expected RGB Code
        String result = Answer.toRGBCode(color);
        assertEquals(expected, result);
    }

    @Test
    public void testToRGBCode_Green() {
        Color color = new Color(0, 255, 0); // Green
        String expected = "#00FF00"; // Expected RGB Code
        String result = Answer.toRGBCode(color);
        assertEquals(expected, result);
    }

    @Test
    public void testToRGBCode_Blue() {
        Color color = new Color(0, 0, 255); // Blue
        String expected = "#0000FF"; // Expected RGB Code
        String result = Answer.toRGBCode(color);
        assertEquals(expected, result);
    }

    @Test
    public void testToRGBCode_CustomColor() {
        Color color = new Color(255, 87, 51); // Custom Color
        String expected = "#FF5733"; // Expected RGB Code
        String result = Answer.toRGBCode(color);
        assertEquals(expected, result);
    }
}