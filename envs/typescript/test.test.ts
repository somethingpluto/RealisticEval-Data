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
    const distance = Math.sqrt(Math.pow(x1 - x2, 2) + Math.pow(y1 - y2, 2));

    return distance;
}

describe('TestCalculateDistance', () => {
    it('should return 0.0 when both agents are at the same point', () => {
        const observations: ObservationData = {
            "agent1": { x: 0, y: 0 },
            "agent2": { x: 0, y: 0 }
        };

        expect(calculateDistance("agent1", "agent2", observations)).toBeCloseTo(0.0);
    });

    it('should return 3.0 when agents are horizontally apart', () => {
        const observations: ObservationData = {
            "agent1": { x: 0, y: 0 },
            "agent2": { x: 3, y: 0 }
        };

        expect(calculateDistance("agent1", "agent2", observations)).toBeCloseTo(3.0);
    });

    it('should return 4.0 when agents are vertically apart', () => {
        const observations: ObservationData = {
            "agent1": { x: 0, y: 0 },
            "agent2": { x: 0, y: 4 }
        };

        expect(calculateDistance("agent1", "agent2", observations)).toBeCloseTo(4.0);
    });

    it('should return the correct diagonal distance', () => {
        const observations: ObservationData = {
            "agent1": { x: 1, y: 2 },
            "agent2": { x: 4, y: 6 }
        };

        const expectedDistance = Math.sqrt(Math.pow(4 - 1, 2) + Math.pow(6 - 2, 2));
        expect(calculateDistance("agent1", "agent2", observations)).toBeCloseTo(expectedDistance);
    });

    it('should return the correct distance with negative coordinates', () => {
        const observations: ObservationData = {
            "agent1": { x: -1, y: -1 },
            "agent2": { x: -4, y: -5 }
        };

        const expectedDistance = Math.sqrt(Math.pow(-4 + 1, 2) + Math.pow(-5 + 1, 2));
        expect(calculateDistance("agent1", "agent2", observations)).toBeCloseTo(expectedDistance);
    });
});
