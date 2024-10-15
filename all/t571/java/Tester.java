package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertTrue;
import static org.junit.Assert.assertFalse;

public class Tester {

    @Test
    public void testValidLatitudeWithDirection() {
        String coord = "45.123N";
        assertTrue(CoordinateValidator.isValidCoordinate(coord));
    }

    @Test
    public void testValidLatitudeWithoutDirection() {
        String coord = "90.0";
        assertTrue(CoordinateValidator.isValidCoordinate(coord));
    }

    @Test
    public void testValidLongitudeWithDirection() {
        String coord = "180.0E";
        assertTrue(CoordinateValidator.isValidCoordinate(coord));
    }

    @Test
    public void testValidLongitudeWithoutDirection() {
        String coord = "-120.456";
        assertTrue(CoordinateValidator.isValidCoordinate(coord));
    }

    @Test
    public void testInvalidLongitudeExceedingRange() {
        String coord = "-200.5";
        assertFalse(CoordinateValidator.isValidCoordinate(coord));
    }
}