
// Test function
function runTests() {
    samples.forEach(({ input, expected }, index) => {
        try {
            const result = zNumber.parse(input);
            if (expected === "error") {
                console.log(`Test ${index + 1} failed: Expected an error, but got ${result}`);
            } else {
                console.log(`Test ${index + 1} passed: Expected ${expected}, got ${result}`);
            }
        } catch (error) {
            if (expected === "error") {
                console.log(`Test ${index + 1} passed: Expected an error and got an error`);
            } else {
                console.log(`Test ${index + 1} failed: Expected ${expected}, but got an error`);
            }
        }
    });
}
