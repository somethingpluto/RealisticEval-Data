package org.real.temp;
import org.junit.Test;
import static org.junit.Assert.assertEquals;
import java.util.Arrays;
import java.util.List;
import static org.real.temp.Answer.*;
public class Tester {

    @Test
    public void testPossibleSingleStation() {
        List<Integer> gas = Arrays.asList(5);
        List<Integer> cost = Arrays.asList(4);
        int expected = 0;
        assertEquals(expected, canCompleteCircuit(gas, cost));
    }

    @Test
    public void testImpossibleSingleStation() {
        List<Integer> gas = Arrays.asList(4);
        List<Integer> cost = Arrays.asList(5);
        int expected = -1;
        assertEquals(expected, canCompleteCircuit(gas, cost));
    }

    @Test
    public void testTwoStationsPossible() {
        List<Integer> gas = Arrays.asList(1, 2);
        List<Integer> cost = Arrays.asList(2, 1);
        int expected = 1;
        assertEquals(expected, canCompleteCircuit(gas, cost));
    }

    @Test
    public void testCircularRoutePossible() {
        List<Integer> gas = Arrays.asList(1, 2, 3, 4, 5);
        List<Integer> cost = Arrays.asList(3, 4, 5, 1, 2);
        int expected = 3;
        assertEquals(expected, canCompleteCircuit(gas, cost));
    }

    @Test
    public void testCircularRouteImpossible() {
        List<Integer> gas = Arrays.asList(2, 3, 4);
        List<Integer> cost = Arrays.asList(3, 4, 3);
        int expected = -1;
        assertEquals(expected, canCompleteCircuit(gas, cost));
    }
}