describe('TestCheckSequences', () => {
    let testFile: string;

    beforeAll(() => {
        // Set up the test cases with sequences
        testFile = 'test_sequences.dat';
        fs.writeFileSync(testFile, "2,4,6,8\n");    // Munodi sequence (d = 2)
        fs.writeFileSync(testFile, "1,3,5,7\n");    // Munodi sequence (d = 2)
        fs.writeFileSync(testFile, "10,20,30\n");   // Munodi sequence (d = 10)
        fs.writeFileSync(testFile, "1,2,4,8\n");    // Not a Munodi sequence (d changes)
        fs.writeFileSync(testFile, "5,10,15,20\n"); // Munodi sequence (d = 5)
    });

    afterAll(() => {
        // Clean up the test file after tests
        fs.unlinkSync(testFile);
    });

    it('should correctly identify Munodi sequences', () => {
        const expectedResults = {
            "2,4,6,8": true,
            "1,3,5,7": true,
            "10,20,30": true,
            "1,2,4,8": false,
            "5,10,15,20": true,
        };

        const results = checkSequences(testFile);

        Object.keys(expectedResults).forEach((seq) => {
            const parsedSeq = seq.split(',').map((num) => parseInt(num, 10));
            expect(results[parsedSeq.toString()]).toEqual(expectedResults[seq]);
        });
    });
});