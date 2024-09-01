/**
 * Splits a list of MIDI note numbers into separate arrays of octaves and root notes.
 *
 * @param {number[]} midiNotes - An array of MIDI note numbers.
 * @returns {Object} An object containing arrays of octaves and root notes.
 */
function separateOctaveAndRoot(midiNotes) {
    if (!Array.isArray(midiNotes) || !midiNotes.every(Number.isInteger)) {
        throw new TypeError('Input must be an array of integers.');
    }

    const octaveNotes = [];
    const rootNotes = [];

    midiNotes.forEach(note => {
        const octave = Math.floor(note / 12);  // Calculate the octave by dividing by 12
        const rootNote = note % 12;            // Calculate the root note as the remainder
        octaveNotes.push(octave);
        rootNotes.push(rootNote);
    });

    return {
        octaveNotes,
        rootNotes
    };
}