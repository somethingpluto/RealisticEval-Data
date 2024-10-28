#define CATCH_CONFIG_MAIN
#include "./lib/catch.hpp"
#include "./solution.cpp"
TEST_CASE("Test Calculate Distance") {
    SECTION("Same Point") {
        // Both agents are at the same point
        std::map<std::string, std::map<std::string, float>> observations = {
            {"agent1", {{"x", 0.0f}, {"y", 0.0f}}},
            {"agent2", {{"x", 0.0f}, {"y", 0.0f}}}
        };
        REQUIRE(calculate_distance("agent1", "agent2", observations) == Approx(0.0f));
    }

    SECTION("Horizontal Distance") {
        // Agents are horizontally apart
        std::map<std::string, std::map<std::string, float>> observations = {
            {"agent1", {{"x", 0.0f}, {"y", 0.0f}}},
            {"agent2", {{"x", 3.0f}, {"y", 0.0f}}}
        };
        REQUIRE(calculate_distance("agent1", "agent2", observations) == Approx(3.0f));
    }

    SECTION("Vertical Distance") {
        // Agents are vertically apart
        std::map<std::string, std::map<std::string, float>> observations = {
            {"agent1", {{"x", 0.0f}, {"y", 0.0f}}},
            {"agent2", {{"x", 0.0f}, {"y", 4.0f}}}
        };
        REQUIRE(calculate_distance("agent1", "agent2", observations) == Approx(4.0f));
    }

    SECTION("Diagonal Distance") {
        // Agents are diagonally apart
        std::map<std::string, std::map<std::string, float>> observations = {
            {"agent1", {{"x", 1.0f}, {"y", 2.0f}}},
            {"agent2", {{"x", 4.0f}, {"y", 6.0f}}}
        };
        float expected_distance = std::sqrt(std::pow(4.0f - 1.0f, 2) + std::pow(6.0f - 2.0f, 2));
        REQUIRE(calculate_distance("agent1", "agent2", observations) == Approx(expected_distance));
    }

    SECTION("Negative Coordinates") {
        // Agents have negative coordinates
        std::map<std::string, std::map<std::string, float>> observations = {
            {"agent1", {{"x", -1.0f}, {"y", -1.0f}}},
            {"agent2", {{"x", -4.0f}, {"y", -5.0f}}}
        };
        float expected_distance = std::sqrt(std::pow(-4.0f + 1.0f, 2) + std::pow(-5.0f + 1.0f, 2));
        REQUIRE(calculate_distance("agent1", "agent2", observations) == Approx(expected_distance));
    }
}