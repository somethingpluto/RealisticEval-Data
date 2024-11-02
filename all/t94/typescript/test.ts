describe('createCircleOfFifths', () => {
    test('should return 12 notes in the circle', () => {
        const result: string[] = createCircleOfFifths('C');
        expect(result).toHaveLength(12);
    });

    test('should start with the given starting note', () => {
        const startingNote: string = 'G';
        const result: string[] = createCircleOfFifths(startingNote);
        expect(result[0]).toBe(startingNote);
    });

    test('should correctly generate the Circle of Fifths starting from C', () => {
        const result: string[] = createCircleOfFifths('C');
        const expectedCircle: string[] = ['C', 'G', 'D', 'A', 'E', 'B', 'F#', 'C#', 'G#', 'D#', 'A#', 'E#'];
        expect(result).toEqual(expectedCircle);
    });

    test('should correctly generate the Circle of Fifths starting from G', () => {
        const result: string[] = createCircleOfFifths('G');
        const expectedCircle: string[] = ['G', 'D', 'A', 'E', 'B', 'F#', 'C#', 'G#', 'D#', 'A#', 'E#', 'B#'];
        expect(result).toEqual(expectedCircle);
    });

    test('should correctly generate the Circle of Fifths starting from F', () => {
        const result: string[] = createCircleOfFifths('F');
        const expectedCircle: string[] = ['F', 'C', 'G', 'D', 'A', 'E', 'B', 'F#', 'C#', 'G#', 'D#', 'A#'];
        expect(result).toEqual(expectedCircle);
    });
});