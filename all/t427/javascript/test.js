describe('TestCheckSequences', () => {
    let testFile;

    beforeAll(() => {
        // Set up the test cases with sequences
        testFile = 'test_sequences.dat';
        fs.writeFileSync(testFile, [
            "2,4,6,8",    // Munodi sequence (d = 2)
            "1,3,5,7",    // Munodi sequence (d = 2)
            "10,20,30",   // Munodi sequence (d = 10)
            "1,2,4,8",    // Not a Munodi sequence (d changes)
            "5,10,15,20"  // Munodi sequence (d = 5)
        ].join('\n'));
    });

    afterAll(() => {
        // Clean up the test file after tests
        fs.unlinkSync(testFile);
    });

    it('should correctly identify Munodi sequences', () => {
        const expectedResults = {
            "[2,4,6,8]": true,
            "[1,3,5,7]": true,
            "[10,20,30]": true,
            "[1,2,4,8]": false,
            "[5,10,15,20]": true,
        };

        const results = checkSequences(testFile);

        Object.keys(expectedResults).forEach(seqStr => {
            const seq = JSON.parse(seqStr);
            expect(results[seqStr]).toEqual(expectedResults[seqStr]);
        });
    });
});