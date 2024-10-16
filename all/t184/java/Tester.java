package org.real.temp;

import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.*;

public class Tester {
    private PriorityQueue pq;

    @Before
    public void setUp() {
        pq = new PriorityQueue();
    }

    @Test
    public void testInsertAndAccessMaximumElement() {
        pq.push(10);
        pq.push(20);
        pq.push(5);
        pq.push(30);
        pq.push(15);

        assertEquals(30, pq.top()); // Ensure the max element is 30
    }

    @Test
    public void testRemoveMaximumElement() {
        pq.push(10);
        pq.push(20);
        pq.push(5);
        pq.push(30);

        pq.pop(); // Remove 30
        assertEquals(20, pq.top()); // Now the max should be 20
        pq.pop(); // Remove 20
        assertEquals(10, pq.top()); // Now the max should be 10
    }

    @Test
    public void testCheckEmptyQueue() {
        assertTrue(pq.isEmpty()); // Initially empty
        pq.push(10);
        assertFalse(pq.isEmpty()); // Now not empty
        pq.pop();
        assertTrue(pq.isEmpty()); // Back to empty
    }

    @Test(expected = RuntimeException.class)
    public void testPopFromEmptyQueue() {
        pq.pop(); // Should throw an error
    }

    @Test(expected = RuntimeException.class)
    public void testAccessTopOfEmptyQueue() {
        pq.top(); // Should throw an error
    }

    @Test
    public void testMaintainMaxHeapProperty() {
        pq.push(3);
        pq.push(1);
        pq.push(4);
        pq.push(2);

        assertEquals(4, pq.top()); // Ensure max is 4

        pq.pop(); // Remove 4
        assertEquals(3, pq.top()); // Now max is 3

        pq.push(5); // Add 5
        assertEquals(5, pq.top()); // Ensure max is now 5
    }
}