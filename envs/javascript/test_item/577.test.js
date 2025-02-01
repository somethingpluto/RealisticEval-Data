/**
 * Formats the post count into a human-readable string.
 * For example:
 *      input: 3 output: 02 Posts
 *      input: 1 output: 01 Post
 *
 * @param {number} count - The number of posts.
 * @returns {string} - A formatted string indicating the number of posts.
 */
function formatPostCount(count) {
    if (count === 0) {
        return "00 Posts";
    } else if (count === 1) {
        return "01 Post";
    } else {
        const formattedCount = count < 10 ? `0${count}` : count;
        return `${formattedCount} Posts`;
    }
}
describe('formatPostCount', () => {
    test('should return "01 Post" for count of 1', () => {
        expect(formatPostCount(1)).toBe('01 Post');
    });

    test('should return "02 Posts" for count of 2', () => {
        expect(formatPostCount(2)).toBe('02 Posts');
    });

    test('should return "10 Posts" for count of 10', () => {
        expect(formatPostCount(10)).toBe('10 Posts');
    });

    test('should return "99 Posts" for count of 99', () => {
        expect(formatPostCount(99)).toBe('99 Posts');
    });

    test('should return "05 Posts" for count of 5', () => {
        expect(formatPostCount(5)).toBe('05 Posts');
    });
});
