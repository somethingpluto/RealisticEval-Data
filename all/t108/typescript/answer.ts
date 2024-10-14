/**
 * Sort the images in ascending order based on their scores and return the reordered image score, name, and ID
 *
 * @param {number[]} imageScores - Array of image scores.
 * @param {string[]} imageNames - Array of image names corresponding to the scores.
 * @param {string[]} imageIDs - Array of image IDs corresponding to the scores.
 * @returns {Object} An object containing the sorted scores, names, and IDs.
 */
function reorderData(
    imageScores: number[],
    imageNames: string[],
    imageIDs: string[]
): { resultScores: number[]; resultNames: string[]; resultIDs: string[] } {
    // Combine the scores, names, and IDs into a single array of objects
    const imageData = imageScores.map((score, index) => ({
        score,
        name: imageNames[index],
        id: imageIDs[index],
    }));

    // Sort the array of objects by score in ascending order
    imageData.sort((a, b) => a.score - b.score);

    // Extract sorted scores, names, and IDs into separate arrays
    const resultScores = imageData.map(data => data.score);
    const resultNames = imageData.map(data => data.name);
    const resultIDs = imageData.map(data => data.id);

    // Return the sorted arrays
    return { resultScores, resultNames, resultIDs };
}