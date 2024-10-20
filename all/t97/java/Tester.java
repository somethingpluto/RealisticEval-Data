package org.real.temp;

import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.*;
import static org.real.temp.Answer.*;

public class Tester {
    private Queue queue;

    @Before
    public void setUp() {
        queue = new Queue();
    }

    @Test
    public void shouldInitializeAnEmptyQueue() {
        assertTrue(queue.isEmpty());
    }

    @Test
    public void shouldEnqueueElementsToTheQueue() {
        queue.enqueue(1);
        queue.enqueue(2);
        queue.enqueue(3);
        assertEquals("1 2 3", queue.printQueue());
        assertFalse(queue.isEmpty());
    }

    @Test
    public void shouldDequeueElementsFromTheQueue() {
        queue.enqueue(1);
        queue.enqueue(2);
        Object dequeuedElement = queue.dequeue();
        assertEquals(1, dequeuedElement);
    }

    @Test
    public void shouldReturnTheFrontElementWithoutRemovingIt() {
        queue.enqueue(10);
        queue.enqueue(20);
        Object frontElement = queue.front();
        assertEquals(10, frontElement);
    }

    @Test
    public void shouldCheckIfTheQueueIsEmpty() {
        assertTrue(queue.isEmpty());
        queue.enqueue(5);
        assertFalse(queue.isEmpty());
        queue.dequeue();
        assertTrue(queue.isEmpty());
    }
}