package org.real.temp;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

public class Tester {

    private UniqueDeque<String> deque;

    @BeforeEach
    public void setUp() {
        deque = new UniqueDeque<>();
    }

    @Test
    public void testAdd() {
        assertTrue(deque.add("item1"));
        assertFalse(deque.add("item1")); // Should not be added again
    }

    @Test
    public void testDelete() {
        deque.add("item1");
        assertTrue(deque.delete("item1"));
        assertFalse(deque.delete("item1")); // Should not be deleted again
    }

    @Test
    public void testContains() {
        deque.add("item1");
        assertTrue(deque.contains("item1"));
        deque.delete("item1");
        assertFalse(deque.contains("item1"));
    }

    @Test
    public void testLength() {
        assertEquals(0, deque.size());
        deque.add("item1");
        assertEquals(1, deque.size());
        deque.add("item2");
        assertEquals(2, deque.size());
        deque.delete("item1");
        assertEquals(1, deque.size());
    }

    @Test
    public void testIterator() {
        deque.add("item1");
        deque.add("item2");
        deque.add("item3");

        int count = 0;
        for (String item : deque) {
            count++;
        }
        assertEquals(3, count);
    }
}