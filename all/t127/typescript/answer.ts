/**
 * Splits a list of MIDI note numbers into separate arrays of octaves and root notes.
 *
 * @param {number[]} midiNotes - An array of MIDI note numbers.
 * @returns {Object} An object containing arrays of octaves and root notes.
 */
function separateOctaveAndRoot(midiNotes: number[]): { octaveNotes: number[]; rootNotes: number[] } {
    if (!Array.isArray(midiNotes) || !midiNotes.every(Number.isInteger)) {
        throw new TypeError('Input must be an array of integers.');
    }

    const octaveNotes: number[] = [];
    const rootNotes: number[] = [];

    midiNotes.forEach(note => {
        const octave = Math.floor(note / 12);
        const rootNote = note % 12;
        octaveNotes.push(octave);
        rootNotes.push(rootNote);
    });

    return {
        octaveNotes,
        rootNotes
    };
}