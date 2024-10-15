package org.real.temp;

import org.junit.Test;

import java.util.ArrayList;
import java.util.List;

import static org.junit.Assert.assertEquals;

public class Tester {

    @Test
    public void testReturnsOriginalArrayWhenElementNotFound() {
        List<Integer> result = Answer.removeElementInArray(List.of(1, 2, 3, 4), 5);
        assertEquals(List.of(1, 2, 3, 4), result);
    }

    @Test
    public void testHandlesEmptyArrayCorrectly() {
        List<Integer> result = Answer.removeElementInArray(new ArrayList<>(), 1);
        assertEquals(new ArrayList<>(), result);
    }

    @Test
    public void testRemovesElementFromArrayOfObjects() {
        Object obj1 = new MyObject(1);
        Object obj2 = new MyObject(2);
        Object obj3 = new MyObject(3);
        List<Object> result = Answer.removeElementInArray(List.of(obj1, obj2, obj3), obj2);
        assertEquals(List.of(obj1, obj3), result);
    }

    @Test
    public void testDoesNotModifyOriginalArray() {
        List<Integer> originalArray = new ArrayList<>(List.of(1, 2, 3));
        List<Integer> result = Answer.removeElementInArray(originalArray, 2);
        assertEquals(List.of(1, 2, 3), originalArray);
        assertEquals(List.of(1, 3), result);
    }

    private static class MyObject {
        private int id;

        public MyObject(int id) {
            this.id = id;
        }

        @Override
        public boolean equals(Object obj) {
            if (this == obj) return true;
            if (obj == null || getClass() != obj.getClass()) return false;
            MyObject myObject = (MyObject) obj;
            return id == myObject.id;
        }

        @Override
        public int hashCode() {
            return Integer.hashCode(id);
        }
    }
}