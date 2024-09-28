#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

// Utility function to find the note name and octave
std::pair<std::string, int> getNoteAndOctave(const std::string& noteName) {
    std::string note = noteName.substr(0, noteName.size() - 1);
    int octave = std::stoi(noteName.substr(noteName.size() - 1));
    return {note, octave};
}

// Utility function to determine if a note is in the C major scale
bool isInCMajor(const std::string& note) {
    static const std::vector<std::string> cMajorScale = {"C", "D", "E", "F", "G", "A", "B"};
    return std::find(cMajorScale.begin(), cMajorScale.end(), note) != cMajorScale.end();
}

// Utility function to transpose a note by a given number of semitones
std::string transpose(const std::string& noteName, int semitones) {
    const std::vector<std::string> chromaticScale = {"C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"};
    auto [note, octave] = getNoteAndOctave(noteName);

    auto it = std::find(chromaticScale.begin(), chromaticScale.end(), note);
    if (it != chromaticScale.end()) {
        int index = std::distance(chromaticScale.begin(), it) + semitones;

        while (index < 0 || index >= chromaticScale.size()) {
            if (index < 0) {
                index += chromaticScale.size();
                octave--;
            }
            if (index >= chromaticScale.size()) {
                index -= chromaticScale.size();
                octave++;
            }
        }
        return chromaticScale[index] + std::to_string(octave);
    }
    return noteName; // Return input if not in chromaticScale
}

std::string adjustToCMajor(const std::string& noteName) {
    auto [note, octave] = getNoteAndOctave(noteName);
    if (!isInCMajor(note)) {
        std::vector<int> searchDirections = {1, -1};
        for (int direction : searchDirections) {
            std::string transposedNote = transpose(noteName, direction);
            auto [transposedNoteName, _] = getNoteAndOctave(transposedNote);
            if (isInCMajor(transposedNoteName))
                return transposedNote;
        }
        return noteName;
    } else {
        return noteName;
    }
}

int main() {
    std::string noteName = "F#4";
    std::string adjustedNote = adjustToCMajor(noteName);
    std::cout << "Adjusted note: " << adjustedNote << std::endl;
    return 0;
}