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