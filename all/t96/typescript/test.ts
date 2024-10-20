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