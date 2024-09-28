// Assuming you have installed the `tonal` package using npm
// npm install tonal

const { Pitch, Scale } = require('tonal');

// Function to adjust a given musical note to the nearest note in the C major scale
function adjustToCMajor(noteName) {
    const cMajorScale = ["C", "D", "E", "F", "G", "A", "B"];

    let givenPitch;
    
    // Attempt to create a Pitch object from the noteName
    try {
        givenPitch = Pitch.create(noteName);
    } catch (error) {
        console.error(`Error: ${error}. Invalid note name provided. Returning 'C4' as a default.`);
        return "C4";
    }

    // If the note is already in the C major scale, return it as is
    if (cMajorScale.includes(Pitch.noteName(givenPitch))) {
        return `${Pitch.noteName(givenPitch)}${Pitch.octave(givenPitch)}`;
    }

    // Attempt to find the closest note in the C major scale, either up or down
    const searchDirections = [1, -1]; // Represents semitone adjustments: up 1 and down 1
    for (let direction of searchDirections) {
        const neighborPitch = Pitch.transpose(givenPitch, direction);
        if (cMajorScale.includes(Pitch.noteName(neighborPitch))) {
            return `${Pitch.noteName(neighborPitch)}${Pitch.octave(neighborPitch)}`;
        }
    }

    // If no close C major note is found, return the original note (this is a fallback, should not generally happen)
    return noteName;
}

// Example usage
console.log(adjustToCMajor("C#4")); // Example input note