// The reorderData function to be tested
function reorderData(imageScores, imageNames, imageIDs) {
    // Combine scores, names, and IDs into an array of objects
    const imageData = imageScores.map((score, index) => ({
        score,
        name: imageNames[index],
        id: imageIDs[index]
    }));

    // Sort imageData by scores in ascending order
    imageData.sort((a, b) => a.score - b.score);

    // Destructure the sorted imageData back into separate arrays
    const resultScores = [];
    const resultNames = [];
    const resultIDs = [];

    imageData.forEach(data => {
        resultScores.push(data.score);
        resultNames.push(data.name);
        resultIDs.push(data.id);
    });

    return { resultScores, resultNames, resultIDs };
}

// Function to run the test samples and verify the results
function runTests() {
    // Test Samples
    const testSamples = [
        {
            imageScores: [90, 85, 95, 88, 92],
            imageNames: ["Image A", "Image B", "Image C", "Image D", "Image E"],
            imageIDs: [1, 2, 3, 4, 5],
            expectedScores: [85, 88, 90, 92, 95],
            expectedNames: ["Image B", "Image D", "Image A", "Image E", "Image C"],
            expectedIDs: [2, 4, 1, 5, 3]
        },
        {
            imageScores: [100, 75, 80, 65, 85],
            imageNames: ["Image F", "Image G", "Image H", "Image I", "Image J"],
            imageIDs: [6, 7, 8, 9, 10],
            expectedScores: [65, 75, 80, 85, 100],
            expectedNames: ["Image I", "Image G", "Image H", "Image J", "Image F"],
            expectedIDs: [9, 7, 8, 10, 6]
        },
        {
            imageScores: [55, 60, 75, 45, 70],
            imageNames: ["Image K", "Image L", "Image M", "Image N", "Image O"],
            imageIDs: [11, 12, 13, 14, 15],
            expectedScores: [45, 55, 60, 70, 75],
            expectedNames: ["Image N", "Image K", "Image L", "Image O", "Image M"],
            expectedIDs: [14, 11, 12, 15, 13]
        },
        {
            imageScores: [10, 20, 30, 40, 50],
            imageNames: ["Image P", "Image Q", "Image R", "Image S", "Image T"],
            imageIDs: [16, 17, 18, 19, 20],
            expectedScores: [10, 20, 30, 40, 50],
            expectedNames: ["Image P", "Image Q", "Image R", "Image S", "Image T"],
            expectedIDs: [16, 17, 18, 19, 20]
        },
        {
            imageScores: [85, 85, 85, 85, 85],
            imageNames: ["Image U", "Image V", "Image W", "Image X", "Image Y"],
            imageIDs: [21, 22, 23, 24, 25],
            expectedScores: [85, 85, 85, 85, 85],
            expectedNames: ["Image U", "Image V", "Image W", "Image X", "Image Y"],
            expectedIDs: [21, 22, 23, 24, 25]
        }
    ];

    // Run tests
    testSamples.forEach((sample, index) => {
        const { resultScores, resultNames, resultIDs } = reorderData(sample.imageScores, sample.imageNames, sample.imageIDs);

        const isCorrectScores = JSON.stringify(resultScores) === JSON.stringify(sample.expectedScores);
        const isCorrectNames = JSON.stringify(resultNames) === JSON.stringify(sample.expectedNames);
        const isCorrectIDs = JSON.stringify(resultIDs) === JSON.stringify(sample.expectedIDs);

        console.log(`Test ${index + 1}:`);
        console.log(`Scores correct: ${isCorrectScores}`);
        console.log(`Names correct: ${isCorrectNames}`);
        console.log(`IDs correct: ${isCorrectIDs}`);
        console.log('-------------------------------');
    });
}

// Execute the tests
runTests();
