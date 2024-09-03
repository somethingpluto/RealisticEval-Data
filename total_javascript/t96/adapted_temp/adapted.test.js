describe('changedClef', () => {
    test('should insert the clef at the correct position when the clef is not specified (default to "bass")', () => {
        const abc = "X:1\nT:Test Tune\nK:C\nC D E F|G A B c|\n";
        const result = changedClef(abc);
        const expected = "X:1\nT:Test Tune\nK:C clef=bass\nC D E F|G A B c|\n";
        expect(result).toBe(expected);
    });

    test('should insert the clef at the correct position when a specific clef is provided', () => {
        const abc = "X:1\nT:Test Tune\nK:C\nC D E F|G A B c|\n";
        const result = changedClef(abc, "treble");
        const expected = "X:1\nT:Test Tune\nK:C clef=treble\nC D E F|G A B c|\n";
        expect(result).toBe(expected);
    });

    test('should handle cases where there is no newline after the key signature.py.py', () => {
        const abc = "X:1\nT:Test Tune\nK:C";
        const result = changedClef(abc, "alto");
        const expected = "X:1\nT:Test Tune\nK:C clef=alto";
        expect(result).toBe(expected);
    });

    test('should not alter the ABC notation if the key signature.py.py is not found', () => {
        const abc = "X:1\nT:Test Tune\nC D E F|G A B c|\n";
        const result = changedClef(abc, "tenor");
        expect(result).toBe(abc); // Expect the original string to be returned unchanged
    });

    test('should correctly handle ABC notation with multiple key signatures', () => {
        const abc = "X:1\nT:Test Tune\nK:G\nG A B c|\nK:D\nD E F# G|\n";
        const result = changedClef(abc, "baritone");
        const expected = "X:1\nT:Test Tune\nK:G clef=baritone\nG A B c|\nK:D\nD E F# G|\n";
        expect(result).toBe(expected);
    });
});
/**
 * modify the ABC string by inserting the specified clef (e.g., "clef=bass") after the tone line (K: ), or "bass" if no clef is specified.
 *
 * @param {string} abc - The ABC notation string.
 * @param {string} [clef="bass"] - The clef to set (default is "bass").
 * @returns {string} - The updated ABC notation string with the new clef.
 */
function changedClef(abc, clef = "bass") {
    let clef_index = abc.indexOf("\nK:");

    // If the key signature.py.py is found
    if (clef_index !== -1) {
        // Find the next newline character after the key signature.py.py line, or if none exists, use the end of the string
        let next_newline = abc.indexOf("\n", clef_index + 1);
        if (next_newline === -1) {
            next_newline = abc.length;
        }

        // Create the string to inject, which includes the clef
        let injection = ` clef=${clef}`;

        // Construct the new ABC string with the injected clef
        return `${abc.substring(0, next_newline)}${injection}${abc.substring(next_newline)}`;
    }

    // If the key signature.py.py is not found, return the original string
    return abc;
}