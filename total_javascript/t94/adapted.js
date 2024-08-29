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