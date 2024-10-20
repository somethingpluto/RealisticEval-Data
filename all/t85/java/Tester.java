package org.real.temp;

import org.junit.Test;

import static org.junit.Assert.assertEquals;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import org.apache.commons.lang3.tuple.Pair;

import static org.real.temp.Answer.*;

public class Tester {

    private static final String COLUMN_A = "A";
    private static final String COLUMN_B = "B";

    @Test
    public void testBasicFilling() {
        List<Pair<String, String>> df = new ArrayList<>(Arrays.asList(
                Pair.of("1", COLUMN_B),
                Pair.of(null, COLUMN_B),
                Pair.of("3", COLUMN_B),
                Pair.of(null, COLUMN_B)
        ));
        List<Pair<String, String>> expected = new ArrayList<>(Arrays.asList(
                Pair.of("1", COLUMN_B),
                Pair.of("foo", COLUMN_B),
                Pair.of("3", COLUMN_B),
                Pair.of("foo", COLUMN_B)
        ));

        List<Pair<String, String>> result = fillMissingWithFirstValid(df, COLUMN_B);
        assertEquals(expected.size(), result.size());
        for (int i = 0; i < expected.size(); i++) {
            assertEquals(expected.get(i).getKey(), result.get(i).getKey());
            assertEquals(expected.get(i).getValue(), result.get(i).getValue());
        }
    }

    @Test
    public void testNoMissingValues() {
        List<Pair<String, String>> df = new ArrayList<>(Arrays.asList(
                Pair.of("1", COLUMN_A),
                Pair.of("2", COLUMN_A),
                Pair.of("3", COLUMN_A)
        ));
        List<Pair<String, String>> expected = new ArrayList<>(Arrays.asList(
                Pair.of("1", COLUMN_A),
                Pair.of("2", COLUMN_A),
                Pair.of("3", COLUMN_A)
        ));

        List<Pair<String, String>> result = fillMissingWithFirstValid(df, COLUMN_A);
        assertEquals(expected.size(), result.size());
        for (int i = 0; i < expected.size(); i++) {
            assertEquals(expected.get(i).getKey(), result.get(i).getKey());
            assertEquals(expected.get(i).getValue(), result.get(i).getValue());
        }
    }

    @Test
    public void testSingleValidValue() {
        List<Pair<String, String>> df = new ArrayList<>(Arrays.asList(
                Pair.of("1", COLUMN_A),
                Pair.of(null, COLUMN_B),
                Pair.of(null, COLUMN_B),
                Pair.of("4", COLUMN_A)
        ));
        List<Pair<String, String>> expected = new ArrayList<>(Arrays.asList(
                Pair.of("1", COLUMN_A),
                Pair.of("bar", COLUMN_B),
                Pair.of("bar", COLUMN_B),
                Pair.of("4", COLUMN_A)
        ));

        List<Pair<String, String>> result = fillMissingWithFirstValid(df, COLUMN_B);
        assertEquals(expected.size(), result.size());
        for (int i = 0; i < expected.size(); i++) {
            assertEquals(expected.get(i).getKey(), result.get(i).getKey());
            assertEquals(expected.get(i).getValue(), result.get(i).getValue());
        }
    }

    @Test
    public void testMultipleValidValues() {
        List<Pair<String, String>> df = new ArrayList<>(Arrays.asList(
                Pair.of("1", COLUMN_A),
                Pair.of(null, COLUMN_B),
                Pair.of("3", COLUMN_A),
                Pair.of("4", COLUMN_A)
        ));
        List<Pair<String, String>> expected = new ArrayList<>(Arrays.asList(
                Pair.of("1", COLUMN_A),
                Pair.of("bar", COLUMN_B),
                Pair.of("3", COLUMN_A),
                Pair.of("4", COLUMN_A)
        ));

        List<Pair<String, String>> result = fillMissingWithFirstValid(df, COLUMN_B);
        assertEquals(expected.size(), result.size());
        for (int i = 0; i < expected.size(); i++) {
            assertEquals(expected.get(i).getKey(), result.get(i).getKey());
            assertEquals(expected.get(i).getValue(), result.get(i).getValue());
        }
    }
}
