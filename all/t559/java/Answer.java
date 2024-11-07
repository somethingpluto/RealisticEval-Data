package org.real.temp;

import java.util.regex.Pattern;

public class Answer {
    /**
     * Checks whether a file name is a C++ header file.
     *
     * @param fileName - The name of the file to check.
     * @returns - Returns true if the file is a C++ header file, false otherwise.
     */
    public static boolean isCppHeaderFile(String fileName) {
        // Define a regular expression to match C++ header file extensions
        Pattern cppHeaderExtensions = Pattern.compile("\\.(h|hh|hpp|hxx)$", Pattern.CASE_INSENSITIVE);
        
        // Test the file name against the regular expression
        return cppHeaderExtensions.matcher(fileName).find();
    }
}