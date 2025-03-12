/**
 * Modify the ABC string by inserting the specified clef (e.g., "clef=bass") 
 * after the tone line (K: ), or "bass" if no clef is specified.
 *
 * @param {string} abc - The ABC notation string.
 * @param {string} [clef="bass"] - The clef to set (default is "bass").
 * @returns {string} - The updated ABC notation string with the new clef.
 */
function changedClef(abc: string, clef: string = "bass"): string {
    // Find the tone line (K: ) in the ABC string
    const toneLineIndex = abc.indexOf('K:');

    // If the tone line is found, insert the clef after it
    if (toneLineIndex !== -1) {
        return abc.slice(0, toneLineIndex + 2) + clef + abc.slice(toneLineIndex + 2);
    }

    // If the tone line is not found, append the clef to the end of the ABC string
    return abc + 'K: ' + clef;
}
describe('changedClef', () => {
    test('should insert the clef at the correct position when the clef is not specified (default to "bass")', () => {
        const abc: string = "X:1\nT:Test Tune\nK:C\nC D E F|G A B c|\n";
        const result: string = changedClef(abc);
        const expected: string = "X:1\nT:Test Tune\nK:C clef=bass\nC D E F|G A B c|\n";
        expect(result).toBe(expected);
    });

    test('should insert the clef at the correct position when a specific clef is provided', () => {
        const abc: string = "X:1\nT:Test Tune\nK:C\nC D E F|G A B c|\n";
        const result: string = changedClef(abc, "treble");
        const expected: string = "X:1\nT:Test Tune\nK:C clef=treble\nC D E F|G A B c|\n";
        expect(result).toBe(expected);
    });

    test('should handle cases where there is no newline after the key signature', () => {
        const abc: string = "X:1\nT:Test Tune\nK:C";
        const result: string = changedClef(abc, "alto");
        const expected: string = "X:1\nT:Test Tune\nK:C clef=alto";
        expect(result).toBe(expected);
    });

    test('should not alter the ABC notation if the key signature is not found', () => {
        const abc: string = "X:1\nT:Test Tune\nC D E F|G A B c|\n";
        const result: string = changedClef(abc, "tenor");
        expect(result).toBe(abc); // Expect the original string to be returned unchanged
    });

    test('should correctly handle ABC notation with multiple key signatures', () => {
        const abc: string = "X:1\nT:Test Tune\nK:G\nG A B c|\nK:D\nD E F# G|\n";
        const result: string = changedClef(abc, "baritone");
        const expected: string = "X:1\nT:Test Tune\nK:G clef=baritone\nG A B c|\nK:D\nD E F# G|\n";
        expect(result).toBe(expected);
    });
});
