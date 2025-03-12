// Additions at the start of the file
import { ImageData } from './ImageData';

// Changes within the function
function reorderData(
    imageScores: number[], 
    imageNames: string[], 
    imageIDs: (string[] | number[]),
    sortBy: 'score' | 'name' = 'score'
): { resultScores: number[], resultNames: string[], resultIDs: (string[] | number[]) } {
    const data: ImageData[] = imageScores.map((score, index) => ({
        score,
        name: imageNames[index],
        id: imageIDs[index]
    }));

    data.sort((a, b) => {
        if (sortBy === 'score') {
            return a.score - b.score;
        } else {
            return a.name.localeCompare(b.name);
        }
    });

    return {
        resultScores: data.map(item => item.score),
        resultNames: data.map(item => item.name),
        resultIDs: data.map(item => item.id)
    };
}
// Additions at the end of the file
describe('reorderData', () => {
    test('sorts question correctly for basic inputs', () => {
        const scores: number[] = [3, 1, 2];
        const names: string[] = ['Image3', 'Image1', 'Image2'];
        const ids: (string | number)[] = [103, 101, 102];
        const expected = {
            resultScores: [1, 2, 3],
            resultNames: ['Image1', 'Image2', 'Image3'],
            resultIDs: [101, 102, 103]
        };
        expect(reorderData(scores, names, ids)).toEqual(expected);
    });

    test('sorts question correctly with mixed scores', () => {
        const scores: number[] = [5, 1, 3, 5, 2];
        const names: string[] = ['Image5', 'Image1', 'Image3', 'Image6', 'Image2'];
        const ids: (string | number)[] = [105, 101, 103, 106, 102];
        const expected = {
            resultScores: [1, 2, 3, 5, 5],
            resultNames: ['Image1', 'Image2', 'Image3', 'Image5', 'Image6'],
            resultIDs: [101, 102, 103, 105, 106]
        };
        expect(reorderData(scores, names, ids)).toEqual(expected);
    });

    test('handles duplicate scores', () => {
        const scores: number[] = [2, 2, 1];
        const names: string[] = ['Image2', 'Image3', 'Image1'];
        const ids: (string | number)[] = [102, 103, 101];
        const expected = {
            resultScores: [1, 2, 2],
            resultNames: ['Image1', 'Image2', 'Image3'],
            resultIDs: [101, 102, 103]
        };
        expect(reorderData(scores, names, ids)).toEqual(expected);
    });

    test('handles empty arrays', () => {
        const scores: number[] = [];
        const names: string[] = [];
        const ids: (string | number)[] = [];
        const expected = {
            resultScores: [],
            resultNames: [],
            resultIDs: []
        };
        expect(reorderData(scores, names, ids)).toEqual(expected);
    });
});
