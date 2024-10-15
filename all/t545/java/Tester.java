package org.real.temp;

import org.junit.Test;
import java.util.Arrays;
import java.util.List;

import static org.junit.Assert.assertEquals;

public class Tester {

    @Test
    public void returnsElementsBeforeTheFirstNull() {
        Object[] inputArray = {"element1", "element2", null, "element3", "element4"};
        List<Object> result = Answer.elementsBeforeNull(inputArray);
        assertEquals(Arrays.asList("element1", "element2"), result);
    }

    @Test
    public void returnsAnEmptyArrayWhenInputIsEmpty() {
        Object[] inputArray = {};
        List<Object> result = Answer.elementsBeforeNull(inputArray);
        assertEquals(Arrays.asList(), result);
    }

    @Test
    public void returnsTheSameArrayIfThereIsNoNull() {
        Object[] inputArray = {"element1", "element2", "element3"};
        List<Object> result = Answer.elementsBeforeNull(inputArray);
        assertEquals(Arrays.asList("element1", "element2", "element3"), result);
    }

    @Test
    public void returnsAnEmptyArrayIfTheFirstElementIsNull() {
        Object[] inputArray = {null, "element2", "element3"};
        List<Object> result = Answer.elementsBeforeNull(inputArray);
        assertEquals(Arrays.asList(), result);
    }

    @Test
    public void handlesMixedTypesWithNull() {
        Object[] inputArray = {1, "text", null, true, false};
        List<Object> result = Answer.elementsBeforeNull(inputArray);
        assertEquals(Arrays.asList(1, "text"), result);
    }

    @Test
    public void handlesAnArrayWithOnlyNull() {
        Object[] inputArray = {null};
        List<Object> result = Answer.elementsBeforeNull(inputArray);
        assertEquals(Arrays.asList(), result);
    }
}