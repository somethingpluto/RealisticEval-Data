/**
 * Merges two arrays of objects, updating items in the first array with items
 * from the second array based on a unique identifier. If an ID exists in both
 * arrays, the item from the second array will replace the one in the first.
 *
 * @param arr1 - The first array of objects to merge.
 * @param arr2 - The second array of objects to merge, which may update
 *               items in the first array.
 * @param getId - A function that takes an object and returns its unique ID
 *                as a string, used to identify items for merging.
 * @returns An array of merged objects, including all unique items from both
 *          input arrays, with updates applied from the second array.
 */
function mergeOrUpdate(arr1, arr2, getId) {
    // Create a map to store items from arr1 indexed by their unique ID
    const map = new Map();

    // Populate the map with items from arr1
    for (const item of arr1) {
        const id = getId(item);
        map.set(id, item);
    }

    // Iterate over arr2 and update or add items to the map
    for (const item of arr2) {
        const id = getId(item);
        map.set(id, item);
    }

    // Convert the map back to an array and return it
    return Array.from(map.values());
}
describe('mergeOrUpdate', () => {
    test('merges two arrays with unique items', () => {
        const arr1 = [
            { id: '1', name: 'Item 1' },
            { id: '2', name: 'Item 2' }
        ];
        const arr2 = [
            { id: '3', name: 'Item 3' },
            { id: '4', name: 'Item 4' }
        ];

        const result = mergeOrUpdate(arr1, arr2, item => item.id);
        expect(result).toEqual([
            { id: '1', name: 'Item 1' },
            { id: '2', name: 'Item 2' },
            { id: '3', name: 'Item 3' },
            { id: '4', name: 'Item 4' }
        ]);
    });

    test('updates existing items when IDs match', () => {
        const arr1 = [
            { id: '1', name: 'Item 1' },
            { id: '2', name: 'Item 2' }
        ];
        const arr2 = [
            { id: '2', name: 'Updated Item 2' },
            { id: '3', name: 'Item 3' }
        ];

        const result = mergeOrUpdate(arr1, arr2, item => item.id);
        expect(result).toEqual([
            { id: '1', name: 'Item 1' },
            { id: '2', name: 'Updated Item 2' },
            { id: '3', name: 'Item 3' }
        ]);
    });

    test('handles empty arrays', () => {
        const arr1 = [];
        const arr2 = [];

        const result = mergeOrUpdate(arr1, arr2, item => item.id);
        expect(result).toEqual([]);
    });

    test('merges with an empty first array', () => {
        const arr1 = [];
        const arr2 = [
            { id: '1', name: 'Item 1' },
            { id: '2', name: 'Item 2' }
        ];

        const result = mergeOrUpdate(arr1, arr2, item => item.id);
        expect(result).toEqual([
            { id: '1', name: 'Item 1' },
            { id: '2', name: 'Item 2' }
        ]);
    });

    test('merges with an empty second array', () => {
        const arr1 = [
            { id: '1', name: 'Item 1' },
            { id: '2', name: 'Item 2' }
        ];
        const arr2 = [];

        const result = mergeOrUpdate(arr1, arr2, item => item.id);
        expect(result).toEqual([
            { id: '1', name: 'Item 1' },
            { id: '2', name: 'Item 2' }
        ]);
    });

    test('handles duplicate IDs in the first array', () => {
        const arr1 = [
            { id: '1', name: 'Item 1' },
            { id: '1', name: 'Duplicate Item 1' } // Duplicate ID
        ];
        const arr2 = [
            { id: '2', name: 'Item 2' }
        ];

        const result = mergeOrUpdate(arr1, arr2, item => item.id);
        expect(result).toEqual([
            { id: '1', name: 'Duplicate Item 1' }, // Last occurrence takes precedence
            { id: '2', name: 'Item 2' }
        ]);
    });

    test('handles duplicate IDs in the second array', () => {
        const arr1 = [
            { id: '1', name: 'Item 1' }
        ];
        const arr2 = [
            { id: '2', name: 'Item 2' },
            { id: '2', name: 'Duplicate Item 2' } // Duplicate ID
        ];

        const result = mergeOrUpdate(arr1, arr2, item => item.id);
        expect(result).toEqual([
            { id: '1', name: 'Item 1' },
            { id: '2', name: 'Duplicate Item 2' } // Last occurrence takes precedence
        ]);
    });

    test('merges arrays with mixed unique and duplicate IDs', () => {
        const arr1 = [
            { id: '1', name: 'Item 1' },
            { id: '2', name: 'Item 2' }
        ];
        const arr2 = [
            { id: '2', name: 'Updated Item 2' },
            { id: '3', name: 'Item 3' },
            { id: '1', name: 'New Item 1' } // Updated item with same ID
        ];

        const result = mergeOrUpdate(arr1, arr2, item => item.id);
        expect(result).toEqual([
            { id: '1', name: 'New Item 1' }, // Updated
            { id: '2', name: 'Updated Item 2' }, // Updated
            { id: '3', name: 'Item 3' }
        ]);
    });
});
