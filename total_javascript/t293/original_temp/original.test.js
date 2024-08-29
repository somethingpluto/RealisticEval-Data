// Function reorderData() was created by ChatGPT and used unedited.
function reorderData(imageScores, imageNames, imageIDs) {
    // Create an array of objects with score, name, and ID
    const imageData = imageScores.map((score, index) => ({
        score,
        name: imageNames[index],
        id: imageIDs[index]
    }));
  
    // Sort the array based on scores in descending order
    imageData.sort((a, b) => b.score - a.score);
  
    // Extract sorted names and IDs into separate arrays
    const resultScores = imageData.map(data => data.score);
    const resultNames = imageData.map(data => data.name);
    const resultIDs = imageData.map(data => data.id);
  
    return { resultScores, resultNames, resultIDs };
}

// Test function
function runTests() {
    // Test Samples
    const testSamples = [
        {
            imageScores: [90, 85, 95, 88, 92],
            imageNames: ["Image A", "Image B", "Image C", "Image D", "Image E"],
            imageIDs: [1, 2, 3, 4, 5],
            expectedScores: [95, 92, 90, 88, 85],
            expectedNames: ["Image C", "Image E", "Image A", "Image D", "Image B"],
            expectedIDs: [3, 5, 1, 4, 2]
        },
        {
            imageScores: [100, 75, 80, 65, 85],
            imageNames: ["Image F", "Image G", "Image H", "Image I", "Image J"],
            imageIDs: [6, 7, 8, 9, 10],
            expectedScores: [100, 85, 80, 75, 65],
            expectedNames: ["Image F", "Image J", "Image H", "Image G", "Image I"],
            expectedIDs: [6, 10, 8, 7, 9]
        },
        {
            imageScores: [55, 60, 75, 45, 70],
            imageNames: ["Image K", "Image L", "Image M", "Image N", "Image O"],
            imageIDs: [11, 12, 13, 14, 15],
            expectedScores: [75, 70, 60, 55, 45],
            expectedNames: ["Image M", "Image O", "Image L", "Image K", "Image N"],
            expectedIDs: [13, 15, 12, 11, 14]
        },
        {
            imageScores: [10, 20, 30, 40, 50],
            imageNames: ["Image P", "Image Q", "Image R", "Image S", "Image T"],
            imageIDs: [16, 17, 18, 19, 20],
            expectedScores: [50, 40, 30, 20, 10],
            expectedNames: ["Image T", "Image S", "Image R", "Image Q", "Image P"],
            expectedIDs: [20, 19, 18, 17, 16]
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
