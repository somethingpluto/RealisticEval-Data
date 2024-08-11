//generated by chatgpt:
function separateOctaveAndRoot(midiNotes) {
      let octaveNotes = [];
      let rootNotes = [];
      midiNotes.forEach(x => {
        let octave = Math.floor(x / 12); // Divide by 12 to get the octave
        let rootNote = x % 12; // The remainder gives the root note within the octave
        octaveNotes.push(octave);
        rootNotes.push(rootNote);
      })
      return {
        octaveNotes,
        rootNotes
      };
    }