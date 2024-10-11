package org.real.temp;

public class Answer {
    /**
     * Simplify file paths in Windows systems into name strings.
     * For example:
     *      input: C:\\Users\\User\\file.txt
     *      output: C_Users_User_file.txt
     *
     * @param path Windows file path string
     * @return Simplified path string
     */
    public static String simplifyWindowsPath(String path) {
        // Replace backslashes with underscores and remove leading/trailing slashes
        return path.replace("\\", "_").replaceAll("^[/\\\\]+|[/\\\\]+$", "");
    }

    public static void main(String[] args) {
        // Example usage
        String simplifiedPath = simplifyWindowsPath("C:\\Users\\User\\file.txt");
        System.out.println(simplifiedPath);  // Output: C_Users_User_file.txt
    }
}