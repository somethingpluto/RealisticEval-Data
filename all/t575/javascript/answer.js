/**
 * Formats the thread count into a user-friendly string.
 * For example:
 *      input: 3 output: 03 Threads
 *      input: 1 output: 01 Thread
 *
 * @param {number} count - The number of threads.
 * @returns {string} - A formatted string indicating the number of threads.
 */
function formatThreadCount(count) {
    // Handle the case when there are no threads
    if (count === 0) {
        return "No Threads";
    }

    // Convert the count to a string and pad it to ensure at least 2 digits
    const threadCount = count.toString().padStart(2, "0");

    // Determine the correct word form based on the count
    const threadWord = count === 1 ? "Thread" : "Threads";

    // Return the formatted string
    return `${threadCount} ${threadWord}`;
}