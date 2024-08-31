describe('ConvertTime Function Tests', () => {
    test('should correctly convert full ISO 8601 duration with hours, minutes, seconds, and milliseconds', () => {
        expect(convertTime('PT1H23M45.678S')).toBe('1h23m45s678ms');
    });

    test('should correctly convert duration with only minutes and seconds including milliseconds', () => {
        expect(convertTime('PT0M30.123S')).toBe('30s123ms');
    });

    test('should correctly convert duration with only seconds and milliseconds', () => {
        expect(convertTime('PT45.5S')).toBe('45s500ms');
    });

    test('should correctly convert duration with hours and minutes, but no seconds', () => {
        expect(convertTime('PT2H5M')).toBe('2h5m');
    });

    test('should correctly convert duration with only seconds, no milliseconds', () => {
        expect(convertTime('PT20S')).toBe('20s');
    });
});