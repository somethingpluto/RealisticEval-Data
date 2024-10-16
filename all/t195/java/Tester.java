package org.real.temp;

import static org.junit.Assert.*;
import org.junit.Before;
import org.junit.Test;

public class Tester {

    private Answer stack;

    @Before
    public void setUp() {
        stack = new Answer(); // Initialize the stack before each test
    }

    // Test Case 1: Pushing and popping a single element
    @Test
    public void testPushAndPopSingleElement() {
        stack.push(3.14f);
        assertEquals(3.14f, stack.pop(), 0.001);
        assertTrue(stack.isEmpty());
    }

    // Test Case 2: Pushing multiple elements and checking peek
    @Test
    public void testPushMultipleAndPeek() {
        stack.push(1.23f);
        stack.push(4.56f);
        assertEquals(4.56f, stack.peek(), 0.001);
        assertEquals(4.56f, stack.pop(), 0.001);
        assertEquals(1.23f, stack.pop(), 0.001);
        assertTrue(stack.isEmpty());
    }

    // Test Case 3: Pop from an empty stack (should throw an exception)
    @Test(expected = IllegalStateException.class)
    public void testPopFromEmptyStack() {
        stack.pop();
    }

    // Test Case 4: Peek on an empty stack (should throw an exception)
    @Test(expected = IllegalStateException.class)
    public void testPeekOnEmptyStack() {
        stack.peek();
    }

    // Test Case 5: Push elements until stack is full and attempt to push another element
    @Test(expected = IllegalStateException.class)
    public void testPushUntilFull() {
        Answer fullStack = new Answer();
        for (int i = 0; i < 100; i++) {
            fullStack.push(i + 0.5f);
        }
        fullStack.push(100.5f); // This should throw an exception
    }
}