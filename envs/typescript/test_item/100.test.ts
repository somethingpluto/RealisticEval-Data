// ... (previous code for context)

function convertTime(duration: string): string {
  const regex = /^P(?:(\d+)Y)?(?:(\d+)M)?(?:(\d+)D)?T?(?:(\d+)H)?(?:(\d+)M)?(?:(\d+(?:\.\d+)?)S)?$/;
  const matches = duration.match(regex);
  if (!matches) {
    throw new Error('Invalid ISO 8601 duration string');
  }

  const parts = matches.slice(1).map(Number).filter(Boolean);
  const partsMap = parts.reduce((acc, part, index) => {
    const unit = ['Y', 'M', 'D', 'H', 'M', 'S', 'ms'];
    acc[unit[index]] = part;
    return acc;
  }, {} as Record<string, number>);

  const readableParts = Object.entries(partsMap)
    .filter(([_, value]) => value > 0)
    .map(([key, value]) => `${value}${key.slice(0, -1)}`); // Remove 's' from 'S'

  return readableParts.join('');
}

// ... (rest of the code)
describe('ConvertTime Function Tests', () => {
    test('should correctly convert full ISO 8601 duration with hours, minutes, seconds, and milliseconds', () => {
        expect(convertTime('PT1H23M45.678S')).toBe('1h23m45s678ms');
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
