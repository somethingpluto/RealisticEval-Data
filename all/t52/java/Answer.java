package org.real.temp;

public class Answer {
    /**
     * Renames a Windows file path by replacing colons in the filename with underscores.
     *
     * @param path The original file path.
     * @return The modified file path with colons in the filename replaced by underscores.
     */
    public static String renameFilePath(String path) {
        return path.replace(":", "_");
    }
}