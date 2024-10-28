package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

import java.util.HashMap;
import java.util.Map;
import static org.real.temp.Answer.*;
public class Tester {

    @Test
    public void testSamePoint() {
        // Both agents are at the same point
        Map<String, Map<String, Double>> observations = new HashMap<>();
        Map<String, Double> agent1Coordinates = new HashMap<>();
        agent1Coordinates.put("x", 0.0);
        agent1Coordinates.put("y", 0.0);
        Map<String, Double> agent2Coordinates = new HashMap<>();
        agent2Coordinates.put("x", 0.0);
        agent2Coordinates.put("y", 0.0);

        observations.put("agent1", agent1Coordinates);
        observations.put("agent2", agent2Coordinates);

        double distance = calculateDistance("agent1", "agent2", observations);
        assertEquals(0.0, distance, 0.001);
    }

    @Test
    public void testHorizontalDistance() {
        // Agents are horizontally apart
        Map<String, Map<String, Double>> observations = new HashMap<>();
        Map<String, Double> agent1Coordinates = new HashMap<>();
        agent1Coordinates.put("x", 0.0);
        agent1Coordinates.put("y", 0.0);
        Map<String, Double> agent2Coordinates = new HashMap<>();
        agent2Coordinates.put("x", 3.0);
        agent2Coordinates.put("y", 0.0);

        observations.put("agent1", agent1Coordinates);
        observations.put("agent2", agent2Coordinates);

        double distance = calculateDistance("agent1", "agent2", observations);
        assertEquals(3.0, distance, 0.001);
    }

    @Test
    public void testVerticalDistance() {
        // Agents are vertically apart
        Map<String, Map<String, Double>> observations = new HashMap<>();
        Map<String, Double> agent1Coordinates = new HashMap<>();
        agent1Coordinates.put("x", 0.0);
        agent1Coordinates.put("y", 0.0);
        Map<String, Double> agent2Coordinates = new HashMap<>();
        agent2Coordinates.put("x", 0.0);
        agent2Coordinates.put("y", 4.0);

        observations.put("agent1", agent1Coordinates);
        observations.put("agent2", agent2Coordinates);

        double distance = calculateDistance("agent1", "agent2", observations);
        assertEquals(4.0, distance, 0.001);
    }

    @Test
    public void testDiagonalDistance() {
        // Agents are diagonally apart
        Map<String, Map<String, Double>> observations = new HashMap<>();
        Map<String, Double> agent1Coordinates = new HashMap<>();
        agent1Coordinates.put("x", 1.0);
        agent1Coordinates.put("y", 2.0);
        Map<String, Double> agent2Coordinates = new HashMap<>();
        agent2Coordinates.put("x", 4.0);
        agent2Coordinates.put("y", 6.0);

        observations.put("agent1", agent1Coordinates);
        observations.put("agent2", agent2Coordinates);

        double expectedDistance = Math.sqrt(Math.pow(4.0 - 1.0, 2) + Math.pow(6.0 - 2.0, 2));
        double distance = calculateDistance("agent1", "agent2", observations);
        assertEquals(expectedDistance, distance, 0.001);
    }

    @Test
    public void testNegativeCoordinates() {
        // Agents have negative coordinates
        Map<String, Map<String, Double>> observations = new HashMap<>();
        Map<String, Double> agent1Coordinates = new HashMap<>();
        agent1Coordinates.put("x", -1.0);
        agent1Coordinates.put("y", -1.0);
        Map<String, Double> agent2Coordinates = new HashMap<>();
        agent2Coordinates.put("x", -4.0);
        agent2Coordinates.put("y", -5.0);

        observations.put("agent1", agent1Coordinates);
        observations.put("agent2", agent2Coordinates);

        double expectedDistance = Math.sqrt(Math.pow(-4.0 + 1.0, 2) + Math.pow(-5.0 + 1.0, 2));
        double distance = calculateDistance("agent1", "agent2", observations);
        assertEquals(expectedDistance, distance, 0.001);
    }
}