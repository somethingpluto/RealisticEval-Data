#define CATCH_CONFIG_MAIN
#include "catch.hpp"
#include <unordered_map>
#include <cmath>
#include <string>

struct Coordinates {
    double x;
    double y;
};

double calculateDistance(const std::string& agent1, const std::string& agent2, const std::unordered_map<std::string, Coordinates>& observations) {
    double x1 = observations.at(agent1).x;
    double y1 = observations.at(agent1).y;
    double x2 = observations.at(agent2).x;
    double y2 = observations.at(agent2).y;

    double distance = std::sqrt(std::pow(x1 - x2, 2) + std::pow(y1 - y2, 2));
    return distance;
}

TEST_CASE("TestCalculateDistance") {
    SECTION("same_point") {
        std::unordered_map<std::string, Coordinates> observations = {
            {"agent1", {0.0, 0.0}},
            {"agent2", {0.0, 0.0}}
        };
        REQUIRE(calculateDistance("agent1", "agent2", observations) == Approx(0.0));
    }

    SECTION("horizontal_distance") {
        std::unordered_map<std::string, Coordinates> observations = {
            {"agent1", {0.0, 0.0}},
            {"agent2", {3.0, 0.0}}
        };
        REQUIRE(calculateDistance("agent1", "agent2", observations) == Approx(3.0));
    }

    SECTION("vertical_distance") {
        std::unordered_map<std::string, Coordinates> observations = {
            {"agent1", {0.0, 0.0}},
            {"agent2", {0.0, 4.0}}
        };
        REQUIRE(calculateDistance("agent1", "agent2", observations) == Approx(4.0));
    }

    SECTION("diagonal_distance") {
        std::unordered_map<std::string, Coordinates> observations = {
            {"agent1", {1.0, 2.0}},
            {"agent2", {4.0, 6.0}}
        };
        double expected_distance = std::sqrt(std::pow(4.0 - 1.0, 2) + std::pow(6.0 - 2.0, 2));
        REQUIRE(calculateDistance("agent1", "agent2", observations) == Approx(expected_distance).epsilon(1e-12));
    }

    SECTION("negative_coordinates") {
        std::unordered_map<std::string, Coordinates> observations = {
            {"agent1", {-1.0, -1.0}},
            {"agent2", {-4.0, -5.0}}
        };
        double expected_distance = std::sqrt(std::pow(-4.0 + 1.0, 2) + std::pow(-5.0 + 1.0, 2));
        REQUIRE(calculateDistance("agent1", "agent2", observations) == Approx(expected_distance).epsilon(1e-12));
    }
}