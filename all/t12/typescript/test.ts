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