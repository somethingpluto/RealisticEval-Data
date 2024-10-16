package org.real.temp;

import static org.junit.Assert.*;
import org.junit.Test;

public class Tester {

    // Test Case 1: Test insertion and extraction of the minimum element
    @Test
    public void testInsertionAndExtractionOfMinimumElement() {
        PriorityQueue pq = new PriorityQueue();

        // Inserting elements into the priority queue
        pq.insert(5);
        pq.insert(2);
        pq.insert(8);
        pq.insert(1);
        pq.insert(3);

        assertEquals(5, pq.size());
        assertEquals(1, pq.peekMin());

        // Extracting the minimum element
        assertEquals(1, pq.extractMin());
        assertEquals(2, pq.extractMin());
        assertEquals(3, pq.extractMin());
        assertEquals(5, pq.extractMin());
        assertEquals(8, pq.extractMin());
        assertTrue(pq.isEmpty());
    }

    // Test Case 2: Test peekMin operation
    @Test
    public void testPeekMinimumElement() {
        PriorityQueue pq = new PriorityQueue();

        pq.insert(10);
        pq.insert(4);
        pq.insert(15);

        assertEquals(4, pq.peekMin());
        assertEquals(3, pq.size()); // Size should remain the same
        assertEquals(4, pq.peekMin()); // Peek should not remove the element
    }

    // Test Case 3: Test edge case of extracting from an empty queue
    @Test(expected = RuntimeException.class)
    public void testExtractFromEmptyQueue() {
        PriorityQueue pq = new PriorityQueue();
        pq.extractMin(); // Should throw exception
    }

    // Test Case 4: Test isEmpty function
    @Test
    public void testCheckIfQueueIsEmpty() {
        PriorityQueue pq = new PriorityQueue();

        assertTrue(pq.isEmpty());

        pq.insert(7);
        assertFalse(pq.isEmpty());

        pq.extractMin();
        assertTrue(pq.isEmpty());
    }

    // Test Case 5: Test multiple insertions and order of extraction
    @Test
    public void testMultipleInsertionsAndExtractionOrder() {
        PriorityQueue pq = new PriorityQueue();

        pq.insert(9);
        pq.insert(4);
        pq.insert(6);
        pq.insert(1);
        pq.insert(8);

        int[] extractedElements = new int[5];
        int index = 0;

        while (!pq.isEmpty()) {
            extractedElements[index++] = pq.extractMin();
        }

        int[] expectedOrder = {1, 4, 6, 8, 9};
        assertArrayEquals(expectedOrder, extractedElements);
    }
}