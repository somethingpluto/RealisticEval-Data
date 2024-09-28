#include <iostream>
#include <unordered_map>
#include <string>
#include <cmath>

struct Coordinates {
    double x;
    double y;
};

double calculateDistance(const std::string& agent1, const std::string& agent2, const std::unordered_map<std::string, Coordinates>& observations) {
    // Extract coordinates of both agents
    double x1 = observations.at(agent1).x;
    double y1 = observations.at(agent1).y;
    double x2 = observations.at(agent2).x;
    double y2 = observations.at(agent2).y;

    // Calculate the Euclidean distance
    double distance = std::sqrt(std::pow(x1 - x2, 2) + std::pow(y1 - y2, 2));

    return distance;
}

int main() {
    // Example usage
    std::unordered_map<std::string, Coordinates> observations = {
        {"agent1", {1.0, 2.0}},
        {"agent2", {4.0, 6.0}}
    };

    double distance = calculateDistance("agent1", "agent2", observations);
    std::cout << "Distance: " << distance << std::endl;

    return 0;
}