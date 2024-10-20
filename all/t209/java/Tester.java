package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.real.temp.Answer.*;
public class Tester {

    @Test
    public void testInsertionAtHead() {
        LinkedList list = new LinkedList();
        list.insertAtHead(10);
        list.insertAtHead(20);
        list.insertAtHead(30);

        // Expected: 30 -> 20 -> 10 -> null
        assertTrue(list.search(10));
        assertTrue(list.search(20));
        assertTrue(list.search(30));
        assertFalse(list.search(40));
    }

    @Test
    public void testInsertionAtTail() {
        LinkedList list = new LinkedList();
        list.insertAtTail(1);
        list.insertAtTail(2);
        list.insertAtTail(3);

        // Expected: 1 -> 2 -> 3 -> null
        assertTrue(list.search(1));
        assertTrue(list.search(2));
        assertTrue(list.search(3));
        assertFalse(list.search(4));
    }

    @Test
    public void testDeletionOfElements() {
        LinkedList list = new LinkedList();
        list.insertAtHead(5);
        list.insertAtHead(10);
        list.insertAtHead(15);

        list.deleteValue(10);
        // Expected: 15 -> 5 -> null
        assertFalse(list.search(10));
        assertTrue(list.search(15));
        assertTrue(list.search(5));

        list.deleteValue(15);
        // Expected: 5 -> null
        assertFalse(list.search(15));
        assertTrue(list.search(5));

        list.deleteValue(5);
        // Expected: null
        assertFalse(list.search(5));
    }

    @Test
    public void testSearchFunctionality() {
        LinkedList list = new LinkedList();
        list.insertAtTail(100);
        list.insertAtTail(200);
        list.insertAtTail(300);

        assertTrue(list.search(100));
        assertTrue(list.search(200));
        assertTrue(list.search(300));
        assertFalse(list.search(400));
    }

    @Test
    public void testEdgeCaseEmptyList() {
        LinkedList list = new LinkedList();

        assertFalse(list.search(1));  // Searching in an empty list
        list.deleteValue(1);          // Deleting from an empty list should not crash
        // Expected: still empty
    }
}