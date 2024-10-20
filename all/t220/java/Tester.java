package org.real.temp;
import org.junit.Test;

import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;

import static org.junit.Assert.*;
import static org.real.temp.Answer.*;

public class Tester {

    @Test
    public void testAddUniqueElements() {
        UniqueDeque ud = new UniqueDeque();
        assertTrue(ud.add(1));
        assertTrue(ud.add(2));
        assertTrue(ud.add(3));
        assertEquals(3, ud.size());
        Iterator<Integer> iterator = ud.iterator();
        List<Integer> list = new LinkedList<>();
        while (iterator.hasNext()) {
            list.add(iterator.next());
        }
        assertEquals("[1, 2, 3]", list.toString());
    }

    @Test
    public void testAddDuplicateElements() {
        UniqueDeque ud = new UniqueDeque();
        assertTrue(ud.add(1));
        assertFalse(ud.add(1));  // Duplicate add should return false
        assertEquals(1, ud.size());
        Iterator<Integer> iterator = ud.iterator();
        List<Integer> list = new LinkedList<>();
        while (iterator.hasNext()) {
            list.add(iterator.next());
        }
        assertEquals("[1]", list.toString());
    }

    @Test
    public void testDeleteElements() {
        UniqueDeque ud = new UniqueDeque();
        ud.add(1);
        ud.add(2);
        ud.add(3);
        assertTrue(ud.delete(2));
        assertFalse(ud.delete(2));  // Deleting non-existing element should return false
        assertEquals(2, ud.size());
        Iterator<Integer> iterator = ud.iterator();
        List<Integer> list = new LinkedList<>();
        while (iterator.hasNext()) {
            list.add(iterator.next());
        }
        assertEquals("[1, 3]", list.toString());
    }

    @Test
    public void testContains() {
        UniqueDeque ud = new UniqueDeque();
        ud.add(1);
        assertTrue(ud.contains(1));
        assertFalse(ud.contains(2));
        ud.delete(1);
        assertFalse(ud.contains(1));
    }

    @Test
    public void testIterAndLen() {
        UniqueDeque ud = new UniqueDeque();
        ud.add(1);
        ud.add(2);
        assertEquals(2, ud.size());
        Iterator<Integer> iterator = ud.iterator();
        List<Integer> list = new LinkedList<>();
        while (iterator.hasNext()) {
            list.add(iterator.next());
        }
        assertEquals("[1, 2]", list.toString());
        ud.delete(1);
        assertEquals(1, ud.size());
        iterator = ud.iterator();
        list.clear();
        while (iterator.hasNext()) {
            list.add(iterator.next());
        }
        assertEquals("[2]", list.toString());
    }
}