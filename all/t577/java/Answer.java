/**
 * Formats the post count into a human-readable string.
 *
 * @param count - The number of posts.
 * @return - A formatted string indicating the number of posts.
 */
public class Answer {
    public static String formatPostCount(int count) {
        if (count == 0) {
            return "No Posts";
        } else {
            String postCount = String.format("%02d", count); // Ensure at least two digits
            String postWord = (count == 1) ? "Post" : "Posts"; // Singular or plural
            return postCount + " " + postWord; // Correctly formatted string
        }
    }

    public static void main(String[] args) {
        System.out.println(formatPostCount(0)); // No Posts
        System.out.println(formatPostCount(1)); // 01 Post
        System.out.println(formatPostCount(5)); // 05 Posts
    }
}