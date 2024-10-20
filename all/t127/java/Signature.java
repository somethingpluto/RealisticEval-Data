/**
 * Splits a list of MIDI note numbers into separate lists of octaves and root notes.
 *
 * @param midiNotes An array of MIDI note numbers.
 * @returns An object containing lists of octaves and root notes.
 */
public static class NoteSeparation {
    public List<Integer> octaveNotes;
    public List<Integer> rootNotes;

    public NoteSeparation(List<Integer> octaveNotes, List<Integer> rootNotes) {
        this.octaveNotes = octaveNotes;
        this.rootNotes = rootNotes;
    }
}
public NoteSeparation separateOctaveAndRoot(int[] midiNotes) {
}