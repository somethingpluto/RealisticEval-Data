function createCircleOfFifths(startingNote: string): string[] {
    let currentNote: string = startingNote;  // Initialize with the starting note
    const circle: string[] = [currentNote];  // Start the circle with the initial note

    // Loop to generate the next 11 notes in the circle
    for (let i = 0; i < 11; i++) {
        // Transpose the current note up by a perfect fifth (P5)
        currentNote = Note.transpose(currentNote, Interval.get("P5"));
        circle.push(currentNote);  // Add the transposed note to the circle
    }

    return circle;  // Return the full Circle of Fifths
}