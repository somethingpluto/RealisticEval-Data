package org.real.temp;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class Tester {

    @Test
    void testHashCode_SameNameAndAge() {
        Answer answer1 = new Answer("Alice", 25);
        Answer answer2 = new Answer("Alice", 25);
        assertEquals(answer1.hashCode(), answer2.hashCode(), "Hash codes should be equal for the same name and age.");
    }

    @Test
    void testHashCode_DifferentName() {
        Answer answer1 = new Answer("Alice", 25);
        Answer answer2 = new Answer("Bob", 25);
        assertNotEquals(answer1.hashCode(), answer2.hashCode(), "Hash codes should be different for different names.");
    }

    @Test
    void testHashCode_DifferentAge() {
        Answer answer1 = new Answer("Alice", 25);
        Answer answer2 = new Answer("Alice", 30);
        assertNotEquals(answer1.hashCode(), answer2.hashCode(), "Hash codes should be different for different ages.");
    }

    @Test
    void testEquals_SameReference() {
        Answer answer = new Answer("Alice", 25);
        assertTrue(answer.equals(answer), "An object should be equal to itself.");
    }

    @Test
    void testEquals_SameNameAndAge() {
        Answer answer1 = new Answer("Alice", 25);
        Answer answer2 = new Answer("Alice", 25);
        assertTrue(answer1.equals(answer2), "Two answers with the same name and age should be equal.");
    }

    @Test
    void testEquals_DifferentName() {
        Answer answer1 = new Answer("Alice", 25);
        Answer answer2 = new Answer("Bob", 25);
        assertFalse(answer1.equals(answer2), "Two answers with different names should not be equal.");
    }

    @Test
    void testEquals_DifferentAge() {
        Answer answer1 = new Answer("Alice", 25);
        Answer answer2 = new Answer("Alice", 30);
        assertFalse(answer1.equals(answer2), "Two answers with different ages should not be equal.");
    }
}
