describe('reorderData', () => {

    test('should reorder the data based on scores in ascending order', () => {
        const imageScores = [90, 85, 95];
        const imageNames = ["image1.png", "image2.png", "image3.png"];
        const imageIDs = ["id1", "id2", "id3"];

        const result = reorderData(imageScores, imageNames, imageIDs);

        expect(result.resultScores).toEqual([85, 90, 95]);
        expect(result.resultNames).toEqual(["image2.png", "image1.png", "image3.png"]);
        expect(result.resultIDs).toEqual(["id2", "id1", "id3"]);
    });

    test('should return the same order if scores are already in ascending order', () => {
        const imageScores = [70, 75, 80];
        const imageNames = ["imageA.png", "imageB.png", "imageC.png"];
        const imageIDs = ["idA", "idB", "idC"];

        const result = reorderData(imageScores, imageNames, imageIDs);

        expect(result.resultScores).toEqual([70, 75, 80]);
        expect(result.resultNames).toEqual(["imageA.png", "imageB.png", "imageC.png"]);
        expect(result.resultIDs).toEqual(["idA", "idB", "idC"]);
    });

    test('should handle an array with only one element', () => {
        const imageScores = [50];
        const imageNames = ["imageSingle.png"];
        const imageIDs = ["idSingle"];

        const result = reorderData(imageScores, imageNames, imageIDs);

        expect(result.resultScores).toEqual([50]);
        expect(result.resultNames).toEqual(["imageSingle.png"]);
        expect(result.resultIDs).toEqual(["idSingle"]);
    });

    test('should handle an empty array', () => {
        const imageScores = [];
        const imageNames = [];
        const imageIDs = [];

        const result = reorderData(imageScores, imageNames, imageIDs);

        expect(result.resultScores).toEqual([]);
        expect(result.resultNames).toEqual([]);
        expect(result.resultIDs).toEqual([]);
    });

    test('should reorder correctly when there are duplicate scores', () => {
        const imageScores = [88, 88, 92];
        const imageNames = ["image1.png", "image2.png", "image3.png"];
        const imageIDs = ["id1", "id2", "id3"];

        const result = reorderData(imageScores, imageNames, imageIDs);

        expect(result.resultScores).toEqual([88, 88, 92]);
        expect(result.resultNames).toEqual(["image1.png", "image2.png", "image3.png"]);
        expect(result.resultIDs).toEqual(["id1", "id2", "id3"]);
    });

});
/**
 * Sort the images in ascending order based on their scores and return the reordered image score, name, and ID
 *
 * @param {number[]} imageScores - Array of image scores.
 * @param {string[]} imageNames - Array of image names corresponding to the scores.
 * @param {string[]} imageIDs - Array of image IDs corresponding to the scores.
 * @returns {Object} An object containing the sorted scores, names, and IDs.
 */
function reorderData(imageScores, imageNames, imageIDs) {
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
