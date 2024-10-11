/**
 * Formats the post count into a human-readable string.
 *
 * @param {number} count - The number of posts.
 * @returns {string} - A formatted string indicating the number of posts.
 */
function formatPostCount(count: number): string {
    if (count === 0) {
        return "No Posts";
    } else {
        const postCount = count.toString().padStart(2, "0"); // Ensure at least two digits
        const postWord = count === 1 ? "Post" : "Posts"; // Singular or plural
        return `${postCount} ${postWord}`; // Correctly formatted string
    }
}