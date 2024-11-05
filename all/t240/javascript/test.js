const { Duration } = require('luxon');

describe('genTimeoutDuration', () => {
    it('should handle single unit days', () => {
        const result = genTimeoutDuration("5d");
        expect(result.as('days')).toBeCloseTo(5);
    });

    it('should handle single unit hours', () => {
        const result = genTimeoutDuration("8h");
        expect(result.as('hours')).toBeCloseTo(8);
    });

    it('should handle single unit minutes', () => {
        const result = genTimeoutDuration("45m");
        expect(result.as('minutes')).toBeCloseTo(45);
    });

    it('should handle single unit seconds', () => {
        const result = genTimeoutDuration("30s");
        expect(result.as('seconds')).toBeCloseTo(30);
    });

    it('should handle complex mix of units', () => {
        const result = genTimeoutDuration("2d 20h 30m");
        expect(result.as('days')).toBeCloseTo(2);
        expect(result.as('hours')).toBeCloseTo(20);
        expect(result.as('minutes')).toBeCloseTo(30);
    });

    it('should handle no units', () => {
        const result = genTimeoutDuration("");
        expect(result.as('milliseconds')).toBeCloseTo(0);
    });
});