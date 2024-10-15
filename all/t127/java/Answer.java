import java.util.ArrayList;
import java.util.List;

public class MidiNoteSeparator {

    public static NoteSeparation separateOctaveAndRoot(int[] midiNotes) {
        if (midiNotes == null) {
            throw new IllegalArgumentException("Input must be an array of integers.");
        }

        List<Integer> octaveNotes = new ArrayList<>();
        List<Integer> rootNotes = new ArrayList<>();

        for (int note : midiNotes) {
            if (note < 0) {
                throw new IllegalArgumentException("MIDI note must be a non-negative integer.");
            }
            int octave = note / 12;  // Calculate the octave
            int rootNote = note % 12; // Calculate the root note
            octaveNotes.add(octave);
            rootNotes.add(rootNote);
        }

        return new NoteSeparation(octaveNotes, rootNotes);
    }

    public static class NoteSeparation {
        public List<Integer> octaveNotes;
        public List<Integer> rootNotes;

        public NoteSeparation(List<Integer> octaveNotes, List<Integer> rootNotes) {
            this.octaveNotes = octaveNotes;
            this.rootNotes = rootNotes;
        }
    }
}