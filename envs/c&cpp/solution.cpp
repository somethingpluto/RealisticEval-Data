#include <iostream>
#include <map>
#include <cmath>
#include <string>

// Function to calculate the Euclidean distance between two agents
float calculate_distance(const std::string& agent1, const std::string& agent2, const std::map<std::string, std::map<std::string, float>>& observations) {
    /**
     * Calculates the Euclidean distance between two agents based on their coordinates in the observations.
     *
     * @param agent1: String representation of agent1's identifier.
     * @param agent2: String representation of agent2's identifier.
     * @param observations: Map containing observation data with agent identifiers as keys.
     *                      Each value is a map with 'x' and 'y' keys representing coordinates.
     * @return: Euclidean distance between the two agents.
     */
    
    // Extract coordinates of both agents
    float x1 = observations.at(agent1).at("x");
    float y1 = observations.at(agent1).at("y");
    float x2 = observations.at(agent2).at("x");
    float y2 = observations.at(agent2).at("y");

    // Calculate the Euclidean distance
    float distance = std::sqrt(std::pow(x1 - x2, 2) + std::pow(y1 - y2, 2));

    return distance;
}