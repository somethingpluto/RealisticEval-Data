#include <iostream>
#include <unordered_map>
#include <cmath>
#include <string>

struct Coordinates {
    double x;
    double y;
};

double calculate_distance(const std::string& agent1, const std::string& agent2,
                          const std::unordered_map<std::string, Coordinates>& observations) {
    // Extract coordinates of both agents
    double x1 = observations.at(agent1).x;
    double y1 = observations.at(agent1).y;
    double x2 = observations.at(agent2).x;
    double y2 = observations.at(agent2).y;

    // Calculate the Euclidean distance
    return std::sqrt(std::pow(x1 - x2, 2) + std::pow(y1 - y2, 2));
}
