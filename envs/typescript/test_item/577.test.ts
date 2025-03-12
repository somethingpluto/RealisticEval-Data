// Add this import statement at the top of your file
import { format } from 'date-fns';

// ... (rest of your existing code)

/**
 * Formats the post count into a human-readable string with optional date.
 * For example:
 *      input: { count: 3, date: new Date() } output: "02 Posts (Today)"
 *      input: { count: 1, date: new Date() } output: "01 Post (Today)"
 *      input: { count: 5, date: null } output: "05 Posts"
 *
 * @param {Object} postInfo - An object containing the number of posts and an optional date.
 * @returns {string} - A formatted string indicating the number of posts and the date if provided.
 */
function formatPostCount(postInfo: { count: number; date?: Date }): string {
  const { count, date } = postInfo;
  const formattedCount = formatCount(count);
  const dateString = date ? format(date, 'PPP') : '';
  return `${formattedCount} Posts${dateString}`;
}

// ... (rest of your existing code)
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
