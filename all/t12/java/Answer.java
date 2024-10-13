package org.real.temp;

import java.util.Map;
import java.util.HashMap;

public class Answer {

    /**
     * Calculates the Euclidean distance between two agents based on their coordinates in the observations.
     *
     * @param agent1      String representation of agent1's identifier.
     * @param agent2      String representation of agent2's identifier.
     * @param observations Map containing observation data with agent identifiers as keys.
     *                     Each value is a Map with 'x' and 'y' keys representing coordinates.
     * @return Euclidean distance between the two agents.
     */
    public static double calculateDistance(String agent1, String agent2, Map<String, Map<String, Double>> observations) {
        // Extract coordinates of both agents
        double x1 = observations.get(agent1).get("x");
        double y1 = observations.get(agent1).get("y");
        double x2 = observations.get(agent2).get("x");
        double y2 = observations.get(agent2).get("y");

        // Calculate the Euclidean distance
        double distance = Math.sqrt(Math.pow(x1 - x2, 2) + Math.pow(y1 - y2, 2));

        return distance;
    }

    public static void main(String[] args) {
        // Example usage
        Map<String, Map<String, Double>> observations = new HashMap<>();
        Map<String, Double> agent1Coordinates = new HashMap<>();
        agent1Coordinates.put("x", 1.0);
        agent1Coordinates.put("y", 2.0);
        Map<String, Double> agent2Coordinates = new HashMap<>();
        agent2Coordinates.put("x", 4.0);
        agent2Coordinates.put("y", 6.0);

        observations.put("agent1", agent1Coordinates);
        observations.put("agent2", agent2Coordinates);

        double distance = calculateDistance("agent1", "agent2", observations);
        System.out.println("The Euclidean distance is: " + distance);
    }
}