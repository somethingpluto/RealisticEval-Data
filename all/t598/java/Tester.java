package org.real.temp;

import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.*;

public class Tester {
    private Queue queue;

    @Before
    public void setUp() {
        queue = new Queue(); // Initialize the queue before each test
    }

    @Test
    public void testInitialQueueIsEmpty() {
        assertTrue("Queue should be empty initially", queue.isEmpty());
    }

    @Test
    public void testEnqueueElements() {
        queue.enqueue(10);
        queue.enqueue(20);
        queue.enqueue(30);

        assertFalse("Queue should not be empty after enqueue", queue.isEmpty());
        assertEquals("Front element should be 10", 10, queue.front());
    }

    @Test
    public void testDequeueElements() {
        queue.enqueue(10);
        queue.enqueue(20);
        queue.enqueue(30);

        int value = queue.dequeue();
        assertEquals("First dequeued element should be 10", 10, value);
        assertEquals("Now front should be 20", 20, queue.front());
    }

    @Test
    public void testDequeueFromEmptyQueue() {
        int value = queue.dequeue();
        assertEquals("Should indicate that the queue is empty", -1, value);
    }

    @Test
    public void testFrontElementOfEmptyQueue() {
        int frontValue = queue.front();
        assertEquals("Should indicate that the queue is empty", -1, frontValue);
    }

    @Test
    public void testQueueBecomesEmptyAfterDequeueingAllElements() {
        queue.enqueue(10);
        queue.enqueue(20);

        queue.dequeue(); // Remove 10
        queue.dequeue(); // Remove 20

        assertTrue("Queue should be empty after dequeuing all elements", queue.isEmpty());
    }
}