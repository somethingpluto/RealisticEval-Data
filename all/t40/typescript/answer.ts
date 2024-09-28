class Pitch {
    name: string;
    octave: number;

    constructor(noteName: string) {
        const regex = /([A-G][#b]?)(\d+)/;
        const match = noteName.match(regex);
        if (!match) throw new Error("Invalid note name");
        this.name = match[1];
        this.octave = parseInt(match[2]);
    }

    get nameWithOctave(): string {
        return `${this.name}${this.octave}`;
    }

    transpose(semitones: number): Pitch {
        const noteNames = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"];
        const index = (noteNames.indexOf(this.name) + semitones + 12) % 12;
        const newName = noteNames[index];
        return new Pitch(`${newName}${this.octave}`);
    }
}

function adjustToCMajor(noteName: string): string {
    const cMajorScale = ["C", "D", "E", "F", "G", "A", "B"];

    let givenPitch: Pitch;
    try {
        givenPitch = new Pitch(noteName);
    } catch (e) {
        console.error(`Error: ${e}. Invalid note name provided. Returning 'C4' as a default.`);
        return "C4";
    }

    if (cMajorScale.includes(givenPitch.name)) {
        return givenPitch.nameWithOctave;
    }

    const searchDirections = [1, -1];
    for (const direction of searchDirections) {
        const neighborPitch = givenPitch.transpose(direction);
        if (cMajorScale.includes(neighborPitch.name)) {
            return neighborPitch.nameWithOctave;
        }
    }

    return noteName;
}