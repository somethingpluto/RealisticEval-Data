package org.real.temp;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class Tester {

    @Test
    public void testLength() {
        String randomString = Answer.generateRandomString();
        assertEquals(25, randomString.length(), "The generated string length should be 25.");
    }

    @Test
    public void testContainsUpperCase() {
        String randomString = Answer.generateRandomString();
        assertTrue(randomString.chars().anyMatch(Character::isUpperCase),
                "The generated string should contain at least one uppercase letter.");
    }

    @Test
    public void testContainsLowerCase() {
        String randomString = Answer.generateRandomString();
        assertTrue(randomString.chars().anyMatch(Character::isLowerCase),
                "The generated string should contain at least one lowercase letter.");
    }

    @Test
    public void testRandomness() {
        String string1 = Answer.generateRandomString();
        String string2 = Answer.generateRandomString();
        assertNotEquals(string1, string2, "Two generated strings should not be the same.");
    }

    @Test
    public void testMultipleGenerations() {
        int numTests = 100;
        boolean hasUpperCase = false;
        boolean hasLowerCase = false;

        for (int i = 0; i < numTests; i++) {
            String randomString = Answer.generateRandomString();
            hasUpperCase |= randomString.chars().anyMatch(Character::isUpperCase);
            hasLowerCase |= randomString.chars().anyMatch(Character::isLowerCase);
        }

        assertTrue(hasUpperCase, "At least one generated string should contain an uppercase letter.");
        assertTrue(hasLowerCase, "At least one generated string should contain a lowercase letter.");
    }
}
