import { v4 as uuidv4 } from 'uuid';

function reorderData(
    imageScores: number[],
    imageNames: string[],
    imageIDs: string[]
): { resultScores: number[]; resultNames: string[]; resultIDs: string[] } {
    // ... existing code ...

    // Add new functionality to handle duplicate scores
    const uniqueScores = new Set(imageScores);
    const scoreToIndexMap = new Map<number, number>();
    uniqueScores.forEach((score, index) => {
        scoreToIndexMap.set(score, index);
    });

    const sortedIndices = imageScores
        .map((score) => scoreToIndexMap.get(score))
        .sort((a, b) => a - b);

    const resultIDs = sortedIndices.map((index) => imageIDs[index]);
    const resultNames = sortedIndices.map((index) => imageNames[index]);
    const resultScores = sortedIndices.map((index) => imageScores[index]);

    // ... existing code ...

    // Add new functionality to assign new unique IDs
    const newImageIDs = resultIDs.map((id, index) => uuidv4());

    return { resultScores, resultNames, newImageIDs };
}
describe('reorderData', () => {
    test('should reorder the question based on scores in ascending order', () => {
        const imageScores: number[] = [90, 85, 95];
        const imageNames: string[] = ["image1.png", "image2.png", "image3.png"];
        const imageIDs: string[] = ["id1", "id2", "id3"];

        const result = reorderData(imageScores, imageNames, imageIDs);

        expect(result.resultScores).toEqual([85, 90, 95]);
        expect(result.resultNames).toEqual(["image2.png", "image1.png", "image3.png"]);
        expect(result.resultIDs).toEqual(["id2", "id1", "id3"]);
    });

    test('should return the same order if scores are already in ascending order', () => {
        const imageScores: number[] = [70, 75, 80];
        const imageNames: string[] = ["imageA.png", "imageB.png", "imageC.png"];
        const imageIDs: string[] = ["idA", "idB", "idC"];

        const result = reorderData(imageScores, imageNames, imageIDs);

        expect(result.resultScores).toEqual([70, 75, 80]);
        expect(result.resultNames).toEqual(["imageA.png", "imageB.png", "imageC.png"]);
        expect(result.resultIDs).toEqual(["idA", "idB", "idC"]);
    });

    test('should handle an array with only one element', () => {
        const imageScores: number[] = [50];
        const imageNames: string[] = ["imageSingle.png"];
        const imageIDs: string[] = ["idSingle"];

        const result = reorderData(imageScores, imageNames, imageIDs);

        expect(result.resultScores).toEqual([50]);
        expect(result.resultNames).toEqual(["imageSingle.png"]);
        expect(result.resultIDs).toEqual(["idSingle"]);
    });

    test('should handle an empty array', () => {
        const imageScores: number[] = [];
        const imageNames: string[] = [];
        const imageIDs: string[] = [];

        const result = reorderData(imageScores, imageNames, imageIDs);

        expect(result.resultScores).toEqual([]);
        expect(result.resultNames).toEqual([]);
        expect(result.resultIDs).toEqual([]);
    });

    test('should reorder correctly when there are duplicate scores', () => {
        const imageScores: number[] = [88, 88, 92];
        const imageNames: string[] = ["image1.png", "image2.png", "image3.png"];
        const imageIDs: string[] = ["id1", "id2", "id3"];

        const result = reorderData(imageScores, imageNames, imageIDs);

        expect(result.resultScores).toEqual([88, 88, 92]);
        expect(result.resultNames).toEqual(["image1.png", "image2.png", "image3.png"]);
        expect(result.resultIDs).toEqual(["id1", "id2", "id3"]);
    });
});
