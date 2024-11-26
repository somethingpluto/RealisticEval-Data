package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import static org.real.temp.Answer.*;
public class Tester {

    @Test
    public void testFlatDict() {
        Map<String, Object> data = new HashMap<>();
        data.put("a", "1");
        data.put("b", "2.5");
        data.put("c", "not a number");

        Map<String, Object> expected = new HashMap<>();
        expected.put("a", 1);
        expected.put("b", 2.5);
        expected.put("c", "not a number");

        assertEquals(expected.toString(), convertStringsToNumbers(data).toString());
    }

    @Test
    public void testNestedDict() {
        Map<String, Object> nestedData = new HashMap<>();
        nestedData.put("y", "10");
        nestedData.put("z", "3.14");

        Map<String, Object> data = new HashMap<>();
        data.put("x", nestedData);
        data.put("w", "20.0");

        Map<String, Object> expectedNestedData = new HashMap<>();
        expectedNestedData.put("y", 10);
        expectedNestedData.put("z", 3.14);

        Map<String, Object> expected = new HashMap<>();
        expected.put("x", expectedNestedData);
        expected.put("w", 20.0);

        assertEquals(expected.toString(), convertStringsToNumbers(data).toString());
    }

    @Test
    public void testListOfStrings() {
        List<Object> data = new ArrayList<>();
        data.add("1");
        data.add("2.5");
        data.add("3");
        data.add("invalid");

        List<Object> expected = new ArrayList<>();
        expected.add(1);
        expected.add(2.5);
        expected.add(3);
        expected.add("invalid");

        assertEquals(expected.toString(), convertStringsToNumbers(data).toString());
    }

    @Test
    public void testMixedStructure() {
        Map<String, Object> nestedData = new HashMap<>();
        nestedData.put("num", "4");

        List<Object> numbers = new ArrayList<>();
        numbers.add("1");
        numbers.add("2.0");
        numbers.add(3);

        List<Object> moreNumbers = new ArrayList<>();
        moreNumbers.add(nestedData);
        moreNumbers.add("5");

        Map<String, Object> data = new HashMap<>();
        data.put("numbers", numbers);
        data.put("more_numbers", moreNumbers);

        List<Object> expectedNumbers = new ArrayList<>();
        expectedNumbers.add(1);
        expectedNumbers.add(2.0);
        expectedNumbers.add(3);

        List<Object> expectedMoreNumbers = new ArrayList<>();
        expectedMoreNumbers.add(nestedData);
        expectedMoreNumbers.add(5);

        Map<String, Object> expected = new HashMap<>();
        expected.put("numbers", expectedNumbers);
        expected.put("more_numbers", expectedMoreNumbers);

        assertEquals(expected.toString(), convertStringsToNumbers(data).toString());
    }

    @Test
    public void testEmptyStructure() {
        Map<String, Object> data = new HashMap<>();

        Map<String, Object> expected = new HashMap<>();

        assertEquals(expected.toString(), convertStringsToNumbers(data).toString());
    }
}
