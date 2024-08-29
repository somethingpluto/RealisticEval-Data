describe('createCircleOfFifths', () => {
    test('should return 12 notes in the circle', () => {
        const result = createCircleOfFifths('C');
        expect(result).toHaveLength(12);
    });

    test('should start with the given starting note', () => {
        const startingNote = 'G';
        const result = createCircleOfFifths(startingNote);
        expect(result[0]).toBe(startingNote);
    });

    test('should correctly generate the Circle of Fifths starting from C', () => {
        const result = createCircleOfFifths('C');
        const expectedCircle = ['C', 'G', 'D', 'A', 'E', 'B', 'F#', 'C#', 'G#', 'D#', 'A#', 'E#'];
        expect(result).toEqual(expectedCircle);
    });

    test('should correctly generate the Circle of Fifths starting from G', () => {
        const result = createCircleOfFifths('G');
        const expectedCircle = ['G', 'D', 'A', 'E', 'B', 'F#', 'C#', 'G#', 'D#', 'A#', 'E#', 'B#'];
        expect(result).toEqual(expectedCircle);
    });

    test('should correctly generate the Circle of Fifths starting from F', () => {
        const result = createCircleOfFifths('F');
        const expectedCircle = ['F', 'C', 'G', 'D', 'A', 'E', 'B', 'F#', 'C#', 'G#', 'D#', 'A#'];
        expect(result).toEqual(expectedCircle);
    });
});
const { Note, Interval } = require('@tonaljs/tonal');

/**
 * generates a cyclic tone sequence of five degrees of length 12 starting with the specified starting note
 *
 * @param {string} startingNote - The musical note to start the Circle of Fifths from (e.g., "C").
 * @returns {string[]} An array representing the Circle of Fifths.
 */
function createCircleOfFifths(startingNote) {
    let currentNote = startingNote;  // Initialize with the starting note
    const circle = [currentNote];    // Start the circle with the initial note

    // Loop to generate the next 11 notes in the circle
    for (let i = 0; i < 11; i++) {
        // Transpose the current note up by a perfect fifth (P5)
        currentNote = Note.transpose(currentNote, Interval.get("P5"));
        circle.push(currentNote);    // Add the transposed note to the circle
    }

    return circle;  // Return the full Circle of Fifths
}