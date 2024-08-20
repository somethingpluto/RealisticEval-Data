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
//generated with ChatGPT
function createCircleOfFifths(startingNote) {
    // Define the starting note (C major)
    let currentNote = startingNote;
    const circle = [currentNote];
    // Loop through 11 times to complete the circle of fifths
    for (let i = 0; i < 11; i++) {
        // Get the next note in the circle (up a perfect fifth)
        currentNote = Note.transpose(currentNote, "P5");
        circle.push(currentNote);
    }
    // Print the circle of fifths
    console.log(circle);
    return circle;
}
