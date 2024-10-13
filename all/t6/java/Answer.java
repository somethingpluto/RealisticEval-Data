package org.real.temp;

import java.nio.file.Path;
import java.nio.file.Paths;

public class Answer {

    /**
     * Simplifies a given Windows path by replacing the drive letter and colon with the drive letter followed by an underscore,
     * replacing all backslashes with underscores, and removing any leading or trailing underscores.
     *
     * @param path The Windows path to be simplified.
     * @return The simplified path.
     */
    public static String simplifyWindowsPath(String path) {
        // Extract the drive letter and the rest of the path
        String[] splitPath = path.split("[:\\\\]", 2);
        String drive = splitPath[0] + "_";

        // Process the rest of the path
        String pathWithoutDrive = splitPath[1];
        String simplifiedPath = pathWithoutDrive.replace("\\", "_").replaceAll("^_|_$", "");

        // Concatenate the simplified drive and path
        String finalPath = drive + simplifiedPath;

        return finalPath;
    }

    // A check function to verify the correctness of the generated function with provided data points
    public static void main(String[] args) {
        System.out.println(simplifyWindowsPath("D:\\User\\Documents")); // Expected: D_User_Documents
        System.out.println(simplifyWindowsPath("C:\\Program Files\\Java")); // Expected: C_Program_Files_Java
        System.out.println(simplifyWindowsPath("E:\\Temp\\")); // Expected: E_Temp
    }
}