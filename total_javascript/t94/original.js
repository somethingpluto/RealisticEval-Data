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
