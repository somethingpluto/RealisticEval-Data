type ObservationData = {
    [agentId: string]: {
        x: number;
        y: number;
    };
};import { Vector2 } from 'three';

/**
 * Calculates the Euclidean distance between two agents based on their coordinates in the observations.
 * ...
 */

function calculateDistance(agent1: string, agent2: string, observations: Record<string, { x: number; y: number }>): number {
  const coords1 = observations[agent1];
  const coords2 = observations[agent2];

  if (!coords1 || !coords2) {
    throw new Error('Observation data for one or both agents is missing.');
  }

  const vector1 = new Vector2(coords1.x, coords1.y);
  const vector2 = new Vector2(coords2.x, coords2.y);

  return vector1.distanceTo(vector2);
}
type ObservationData = {
    [agentId: string]: {
        x: number;
        y: number;
    };
};
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
