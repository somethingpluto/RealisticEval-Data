package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertTrue;
import static org.junit.Assert.assertFalse;
import static org.real.temp.Answer.*;
import java.util.Set;
import java.util.TreeSet;
import java.util.Arrays;

public class Tester {
    @Test
    public void testIdenticalSets() {
        Set<Double> set1 = new TreeSet<>(Arrays.asList(1.0, 2.0, 3.0));
        Set<Double> set2 = new TreeSet<>(Arrays.asList(1.0, 2.0, 3.0));
        assertTrue("Two identical sets should be equal", areSetsEqual(set1, set2, 1e-5, 1e-6));
    }

    @Test
    public void testSetsWithCloseValues() {
        Set<Double> set1 = new TreeSet<>(Arrays.asList(1.0, 2.00001, 3.0));
        Set<Double> set2 = new TreeSet<>(Arrays.asList(1.0, 2.00002, 3.0));
        assertTrue("Two sets with close values should be equal", areSetsEqual(set1, set2, 1e-5, 1e-6));
    }

    @Test
    public void testSetsWithLargeDifference() {
        Set<Double> set1 = new TreeSet<>(Arrays.asList(1.0, 2.0, 3.0));
        Set<Double> set2 = new TreeSet<>(Arrays.asList(1.0, 2.5, 3.0));
        assertFalse("Two sets with large differences should not be equal", areSetsEqual(set1, set2, 1e-5, 1e-6));
    }

    @Test
    public void testSetsWithOneDifferentValue() {
        Set<Double> set1 = new TreeSet<>(Arrays.asList(1.0, 2.0, 3.0));
        Set<Double> set2 = new TreeSet<>(Arrays.asList(1.0, 2.000001, 3.0));
        assertTrue("Two sets with one different value should be equal", areSetsEqual(set1, set2, 1e-5, 1e-6));
    }

    @Test
    public void testEmptySets() {
        Set<Double> set1 = new TreeSet<>();
        Set<Double> set2 = new TreeSet<>();
        assertTrue("Two empty sets should be equal", areSetsEqual(set1, set2, 1e-5, 1e-6));
    }
}