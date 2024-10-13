import * as math from 'mathjs';

// Define the type for the observation data
type ObservationData = {
    [agentId: string]: {
        x: number;
        y: number;
    };
};

/**
 * Calculates the Euclidean distance between two agents based on their coordinates in the observations.
 * 
 * @param agent1 - String representation of agent1's identifier.
 * @param agent2 - String representation of agent2's identifier.
 * @param observations - Dictionary containing observation data with agent identifiers as keys.
 *                       Each value is an object with 'x' and 'y' properties representing coordinates.
 * @returns The Euclidean distance between the two agents.
 */
function calculateDistance(agent1: string, agent2: string, observations: ObservationData): number {
    // Extract coordinates of both agents
    const { x: x1, y: y1 } = observations[agent1];
    const { x: x2, y: y2 } = observations[agent2];

    // Calculate the Euclidean distance
    const distance = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2));

    return distance;
}
