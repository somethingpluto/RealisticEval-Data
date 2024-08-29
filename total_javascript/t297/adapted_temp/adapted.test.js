/**
 * Create a mosaic of a given p5.js sketch.
 * Created using ChatGPT-3.5-turbo:
 * https://chat.openai.com/share/a88e18c4-7a2f-467f-9933-53df1d5faf3e
 */
function createIframe(url, size) {
    const iframe = document.createElement('iframe');
    iframe.src = url;
    iframe.style.width = `${size}px`;
    iframe.style.height = `${size}px`;

    iframe.addEventListener('load', () => {
        iframe.classList.add('fade-in');
    });

    document.body.appendChild(iframe);
}

// Test samples
const testSamples = [
    { url: 'https://example.com/1', size: 200 },
    { url: 'https://example.com/2', size: 300 },
    { url: 'https://example.com/3', size: 400 },
    { url: 'https://example.com/4', size: 500 },
    { url: 'https://example.com/5', size: 600 },
];

// Function to run the test samples and verify the results
function runTests() {
    testSamples.forEach((sample, index) => {
        createIframe(sample.url, sample.size);

        // Assume the iframe is the last child in the body
        const iframe = document.body.lastChild;

        // Check the iframe's properties
        const isSrcCorrect = iframe.src === sample.url;
        const isWidthCorrect = iframe.style.width === `${sample.size}px`;
        const isHeightCorrect = iframe.style.height === `${sample.size}px`;

        console.log(`Test ${index + 1}:`);
        console.log(`URL is correct: ${isSrcCorrect}`);
        console.log(`Width is correct: ${isWidthCorrect}`);
        console.log(`Height is correct: ${isHeightCorrect}`);
        console.log('-------------------------------');
    });
}

// Execute the tests
runTests();