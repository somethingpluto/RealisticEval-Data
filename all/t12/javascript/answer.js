function calculateDistance(agent1, agent2, observations) {
    /**
     * Calculates the Euclidean distance between two agents based on their coordinates in the observations.
     *
     * @param {string} agent1 - String representation of agent1's identifier.
     * @param {string} agent2 - String representation of agent2's identifier.
     * @param {Object} observations - Dictionary containing observation questions with agent identifiers as keys.
     *                                Each value is an object with 'x' and 'y' keys representing coordinates.
     * @return {number} Euclidean distance between the two agents.
     */
    
    // Extract coordinates of both agents
    const x1 = observations[agent1].x;
    const y1 = observations[agent1].y;
    const x2 = observations[agent2].x;
    const y2 = observations[agent2].y;
    
    // Calculate the Euclidean distance
    const distance = Math.sqrt(Math.pow((x1 - x2), 2) + Math.pow((y1 - y2), 2));
    
    return distance;
}