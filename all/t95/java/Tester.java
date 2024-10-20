package org.real.temp;

import org.junit.Test;

import java.util.List;
import java.util.function.Predicate;

import static org.junit.Assert.assertEquals;
import static org.real.temp.Answer.findMatchingElements;

public class Tester {

    @Test
    public void testEmptyArray() {
        List<Answer.MatchResult> result = findMatchingElements(new Object[]{}, el -> false);
        assertEquals(0, result.size());
    }

    @Test
    public void testMatchingElementsAndIndices() {
        Object[] inputArray = {1, 2, 3, 4, 5};
        Predicate<Object> comparisonFunction = num -> (Integer) num > 3;
        List<Answer.MatchResult> result = findMatchingElements(inputArray, comparisonFunction);
        assertEquals(2, result.size());
        assertEquals(4, result.get(0).getElement());
        assertEquals(3, result.get(0).getIndex());
        assertEquals(5, result.get(1).getElement());
        assertEquals(4, result.get(1).getIndex());
    }

    @Test
    public void testStringMatchingCondition() {
        Object[] inputArray = {"apple", "banana", "cherry", "date"};
        Predicate<Object> comparisonFunction = fruit -> ((String) fruit).startsWith("b");
        List<Answer.MatchResult> result = findMatchingElements(inputArray, comparisonFunction);
        assertEquals(1, result.size());
        assertEquals("banana", result.get(0).getElement());
        assertEquals(1, result.get(0).getIndex());
    }

    @Test
    public void testMultipleElementsWithSameValue() {
        Object[] inputArray = {1, 2, 2, 3, 2, 4};
        Predicate<Object> comparisonFunction = num -> (Integer) num == 2;
        List<Answer.MatchResult> result = findMatchingElements(inputArray, comparisonFunction);
        assertEquals(3, result.size());
        assertEquals(2, result.get(0).getElement());
        assertEquals(1, result.get(0).getIndex());
        assertEquals(2, result.get(1).getElement());
        assertEquals(2, result.get(1).getIndex());
        assertEquals(2, result.get(2).getElement());
        assertEquals(4, result.get(2).getIndex());
    }

    @Test
    public void testMatchingObjectsByProperty() {
        Object[] inputArray = {
                new Person("Alice", 25),
                new Person("Bob", 30),
                new Person("Charlie", 30)
        };
        Predicate<Object> comparisonFunction = person -> ((Person) person).getAge() == 30;
        List<Answer.MatchResult> result = findMatchingElements(inputArray, comparisonFunction);
        assertEquals(2, result.size());
        assertEquals("Bob", ((Person) result.get(0).getElement()).getName());
        assertEquals(1, result.get(0).getIndex());
        assertEquals("Charlie", ((Person) result.get(1).getElement()).getName());
        assertEquals(2, result.get(1).getIndex());
    }

    @Test
    public void testNoMatchesFound() {
        Object[] inputArray = {1, 3, 5, 7};
        Predicate<Object> comparisonFunction = num -> (Integer) num % 2 == 0;
        List<Answer.MatchResult> result = findMatchingElements(inputArray, comparisonFunction);
        assertEquals(0, result.size());
    }

    @Test
    public void testNegativeNumbers() {
        Object[] inputArray = {-1, -2, 0, 1, 2};
        Predicate<Object> comparisonFunction = num -> (Integer) num < 0;
        List<Answer.MatchResult> result = findMatchingElements(inputArray, comparisonFunction);
        assertEquals(2, result.size());
        assertEquals(-1, result.get(0).getElement());
        assertEquals(0, result.get(0).getIndex());
        assertEquals(-2, result.get(1).getElement());
        assertEquals(1, result.get(1).getIndex());
    }

    // Simple Person class for testing
    public static class Person {
        private String name;
        private int age;

        public Person(String name, int age) {
            this.name = name;
            this.age = age;
        }

        public String getName() {
            return name;
        }

        public int getAge() {
            return age;
        }
    }
}