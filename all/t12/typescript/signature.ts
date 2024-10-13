/**
 * Calculates the Euclidean distance between two agents based on their coordinates in the observations.
 *
 * @param agent1 - String representation of agent1's identifier.
 * @param agent2 - String representation of agent2's identifier.
 * @param observations - Dictionary containing observation data with agent identifiers as keys.
 *                       Each value is an object with 'x' and 'y' properties representing coordinates.
 * @returns The Euclidean distance between the two agents.
 */
function calculateDistance(agent1: string, agent2: string, observations: Record<string, { x: number; y: number }>): number {