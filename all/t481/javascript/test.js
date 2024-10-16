describe("printBoard outputs correct format", () => {
    const board1 = [
        ['X', 'O', 'X'],
        [' ', 'X', 'O'],
        ['O', ' ', ' ']
    ];

    const board2 = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ];

    const board3 = [
        ['X', 'X', 'X'],
        ['O', 'O', ' '],
        [' ', ' ', ' ']
    ];

    const board4 = [
        ['O', 'O', 'O'],
        ['X', 'X', 'X'],
        ['X', 'O', ' ']
    ];

    const board5 = [
        ['X', ' ', ' '],
        [' ', 'X', ' '],
        [' ', ' ', 'X']
    ];

    const board6 = [
        [' ', 'O', ' '],
        ['O', ' ', 'O'],
        [' ', 'O', ' ']
    ];

    // Helper function to capture console output
    function captureOutput(fn, ...args) {
        const originalLog = console.log;
        let output = '';
        console.log = (msg) => {
            output += msg + '\n';
        };
        fn(...args);
        console.log = originalLog;
        return output;
    }

    test("Test case 1", () => {
        const expectedOutput = "-------------\n| X | O | X | \n-------------\n|   | X | O | \n-------------\n| O |   |   | \n-------------\n";
        const output = captureOutput(printBoard, board1);
        expect(output).toBe(expectedOutput);
    });

    test("Test case 2", () => {
        const expectedOutput = "-------------\n|   |   |   | \n-------------\n|   |   |   | \n-------------\n|   |   |   | \n-------------\n";
        const output = captureOutput(printBoard, board2);
        expect(output).toBe(expectedOutput);
    });

    test("Test case 3", () => {
        const expectedOutput = "-------------\n| X | X | X | \n-------------\n| O | O |   | \n-------------\n|   |   |   | \n-------------\n";
        const output = captureOutput(printBoard, board3);
        expect(output).toBe(expectedOutput);
    });

    test("Test case 4", () => {
        const expectedOutput = "-------------\n| O | O | O | \n-------------\n| X | X | X | \n-------------\n| X | O |   | \n-------------\n";
        const output = captureOutput(printBoard, board4);
        expect(output).toBe(expectedOutput);
    });

    test("Test case 5", () => {
        const expectedOutput = "-------------\n| X |   |   | \n-------------\n|   | X |   | \n-------------\n|   |   | X | \n-------------\n";
        const output = captureOutput(printBoard, board5);
        expect(output).toBe(expectedOutput);
    });

    test("Test case 6", () => {
        const expectedOutput = "-------------\n|   | O |   | \n-------------\n| O |   | O | \n-------------\n|   | O |   | \n-------------\n";
        const output = captureOutput(printBoard, board6);
        expect(output).toBe(expectedOutput);
    });
});