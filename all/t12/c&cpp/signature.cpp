/**
 * Calculates the Euclidean distance between two agents based on their coordinates in the observations.
 *
 * @param agent1 The string representation of agent1's identifier.
 * @param agent2 The string representation of agent2's identifier.
 * @param observations A map containing observation questions with agent identifiers as keys. Each value is a struct or class with 'x' and 'y' members representing coordinates.
 * @return The Euclidean distance between the two agents.
 */
double calculate_distance(const std::string& agent1, const std::string& agent2,
                          const std::unordered_map<std::string, Coordinates>& observations) {}