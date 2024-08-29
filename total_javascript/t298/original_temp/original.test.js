
/* function created using chatGPT */
function setEurValue(value) {
    if (value === '' || value === null) return '';
    let number = parseInt(value);
    if (isNaN(number)) return '';
    if (number >= 1000000) {
        return (number / 1000000).toFixed(1) + 'm';
    } else if (number >= 1000) {
        return (number / 1000).toFixed(1) + 'k';
    } else {
        return number.toString();
    }
}

// Function to run test samples and check results
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

