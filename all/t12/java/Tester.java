package org.real.temp;
import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.HashMap;
import java.util.Map;

import org.junit.jupiter.api.Test;

public class Tester {
    @Test
    public void testSamePoint() {
        // Both agents are at the same point
        Map<String, Map<String, Integer>> observations = new HashMap<>();
        observations.put("agent1", new HashMap<>() {{ put("x", 0); put("y", 0); }});
        observations.put("agent2", new HashMap<>() {{ put("x", 0); put("y", 0); }});

        assertEquals(0.0, calculateDistance("agent1", "agent2", observations), 0.0001);
    }

    @Test
    public void testHorizontalDistance() {
        // Agents are horizontally apart
        Map<String, Map<String, Integer>> observations = new HashMap<>();
        observations.put("agent1", new HashMap<>() {{ put("x", 0); put("y", 0); }});
        observations.put("agent2", new HashMap<>() {{ put("x", 3); put("y", 0); }});

        assertEquals(3.0, calculateDistance("agent1", "agent2", observations), 0.0001);
    }

    @Test
    public void testVerticalDistance() {
        // Agents are vertically apart
        Map<String, Map<String, Integer>> observations = new HashMap<>();
        observations.put("agent1", new HashMap<>() {{ put("x", 0); put("y", 0); }});
        observations.put("agent2", new HashMap<>() {{ put("x", 0); put("y", 4); }});

        assertEquals(4.0, calculateDistance("agent1", "agent2", observations), 0.0001);
    }

    @Test
    public void testDiagonalDistance() {
        // Agents are diagonally apart
        Map<String, Map<String, Integer>> observations = new HashMap<>();
        observations.put("agent1", new HashMap<>() {{ put("x", 1); put("y", 2); }});
        observations.put("agent2", new HashMap<>() {{ put("x", 4); put("y", 6); }});

        double expectedDistance = Math.sqrt(Math.pow(4 - 1, 2) + Math.pow(6 - 2, 2));
        assertEquals(expectedDistance, calculateDistance("agent1", "agent2", observations), 0.0001);
    }

    @Test
    public void testNegativeCoordinates() {
        // Agents have negative coordinates
        Map<String, Map<String, Integer>> observations = new HashMap<>();
        observations.put("agent1", new HashMap<>() {{ put("x", -1); put("y", -1); }});
        observations.put("agent2", new HashMap<>() {{ put("x", -4); put("y", -5); }});

        double expectedDistance = Math.sqrt(Math.pow(-4 + 1, 2) + Math.pow(-5 + 1, 2));
        assertEquals(expectedDistance, calculateDistance("agent1", "agent2", observations), 0.0001);
    }
}
