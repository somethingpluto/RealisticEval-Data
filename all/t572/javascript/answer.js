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
    // Create a Map to store unique items based on their IDs
    const itemMap = new Map();

    // Helper function to add items to the map
    const addItemsToMap = (arr) => {
        arr.forEach(item => {
            const id = getId(item);
            itemMap.set(id, item); // Set the item in the map, replacing if it already exists
        });
    };

    // Add items from both arrays to the map
    addItemsToMap(arr1);
    addItemsToMap(arr2);

    // Convert the map values back to an array and return
    return Array.from(itemMap.values());
}