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
    // Convert the count to a string and pad with leading zeros if necessary
    const paddedCount = count.toString().padStart(2, '0');
    
    // Determine the correct pluralization of "Thread"
    const threadLabel = count === 1 ? 'Thread' : 'Threads';
    
    // Return the formatted string
    return `${paddedCount} ${threadLabel}`;
}
describe('formatThreadCount', () => {
    test('should return "01 Thread" for a count of 1', () => {
        expect(formatThreadCount(1)).toBe("01 Thread");
    });

    test('should return "05 Threads" for a count of 5', () => {
        expect(formatThreadCount(5)).toBe("05 Threads");
    });

    test('should return "10 Threads" for a count of 10', () => {
        expect(formatThreadCount(10)).toBe("10 Threads");
    });

    test('should return "99 Threads" for a count of 99', () => {
        expect(formatThreadCount(99)).toBe("99 Threads");
    });
});
