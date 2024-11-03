/**
 * Finds two indices of numbers in the array that sum up to the target value.
 *
 * @param {number[]} nums - The input array of integers.
 * @param {number} target - The target sum value.
 * @returns {number[]} - An array containing the indices of the two numbers.
 * @throws {Error} - If no such indices are found.
 */
function twoSum(nums: number[], target: number): number[] {
    // Create a map to store numbers and their corresponding indices
    const numsMap: { [key: number]: number } = {};

    // First loop to populate the map
    for (let i = 0; i < nums.length; i++) {
        numsMap[nums[i]] = i;
    }

    // Second loop to find the two indices
    for (let i = 0; i < nums.length; i++) {
        const complement = target - nums[i]; // Calculate the complement

        // Check if the complement exists and is not the same index
        if (complement in numsMap && numsMap[complement] !== i) {
            return [i, numsMap[complement]]; // Return the indices
        }
    }

    // If no solution is found, throw an error
    throw new Error("No two sum solution");
}