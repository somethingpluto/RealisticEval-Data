describe('separateOctaveAndRoot', () => {
    test('correctly separates MIDI notes into octaves and root notes', () => {
        const midiNotes: number[] = [60, 61, 62];  // C4, C#4, D4
        const expected = {
            octaveNotes: [5, 5, 5],  // All notes are in the 5th octave
            rootNotes: [0, 1, 2]     // Root notes are C, C#, D
        };
        expect(separateOctaveAndRoot(midiNotes)).toEqual(expected);
    });

    test('handles single MIDI note input', () => {
        const midiNotes: number[] = [24];  // C1
        const expected = {
            octaveNotes: [2],  // 2nd octave
            rootNotes: [0]     // C note
        };
        expect(separateOctaveAndRoot(midiNotes)).toEqual(expected);
    });

    test('returns empty arrays for an empty input array', () => {
        const midiNotes: number[] = [];
        const expected = {
            octaveNotes: [],
            rootNotes: []
        };
        expect(separateOctaveAndRoot(midiNotes)).toEqual(expected);
    });

    test('throws an error for invalid input types', () => {
        const invalidInput = "not an array";
        expect(() => separateOctaveAndRoot(invalidInput as any)).toThrow(TypeError);
        expect(() => separateOctaveAndRoot([3.14] as any)).toThrow(TypeError);
    });

    test('handles MIDI notes from different octaves', () => {
        const midiNotes: number[] = [12, 25, 37];  // C1, C#2, D#3
        const expected = {
            octaveNotes: [1, 2, 3],  // 1st, 2nd, and 3rd octaves
            rootNotes: [0, 1, 1]     // Root notes are C, C#, D#
        };
        expect(separateOctaveAndRoot(midiNotes)).toEqual(expected);
    });
});