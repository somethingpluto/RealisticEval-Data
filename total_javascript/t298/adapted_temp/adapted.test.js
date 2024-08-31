/* function created using chatGPT */
function setEurValue(value) {
    if (!value) return '';
    
    const number = parseInt(value, 10);
    if (isNaN(number)) return '';

    if (number >= 1_000_000) {
        return `${(number / 1_000_000).toFixed(1)}m`;
    } else if (number >= 1_000) {
        return `${(number / 1_000).toFixed(1)}k`;
    } else {
        return `${number}`;
    }
}

// Function to run test.js samples and check results
function runTests() {
    const testSamples = [
        { input: '1500000', expected: '1.5m' },
        { input: '7500', expected: '7.5k' },
        { input: '450', expected: '450' },
        { input: '', expected: '' },
        { input: 'abcd', expected: '' }
    ];

    testSamples.forEach((sample, index) => {
        const result = setEurValue(sample.input);
        const isCorrect = result === sample.expected;

        console.log(`Test ${index + 1}:`);
        console.log(`Input: ${sample.input}`);
        console.log(`Expected: ${sample.expected}`);
        console.log(`Result: ${result}`);
        console.log(`Test Passed: ${isCorrect}`);
        console.log('-------------------------------');
    });
}

// Execute the tests
runTests();
