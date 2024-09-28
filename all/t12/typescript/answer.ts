function calculateDistance(agent1: string, agent2: string, observations: Record<string, { x: number; y: number }>): number {
    // Extract coordinates of both agents
    const { x: x1, y: y1 } = observations[agent1];
    const { x: x2, y: y2 } = observations[agent2];

    // Calculate the Euclidean distance
    const distance = Math.sqrt(Math.pow(x1 - x2, 2) + Math.pow(y1 - y2, 2));

    return distance;
}