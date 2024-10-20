package org.real.temp;
public class Answer {
    public static String getFileExtension(String fileName) {
        // Regex to match the portion after the last dot in the filename
        String regex = "(?:\\.([^.]+))?$";
        java.util.regex.Pattern pattern = java.util.regex.Pattern.compile(regex);
        java.util.regex.Matcher matcher = pattern.matcher(fileName);

        // Return the captured group (extension) if it exists
        if (matcher.find() && matcher.group(1) != null) {
            return matcher.group(1);
        }

        // Return an empty string if no extension is found
        return "";
    }

    public static void main(String[] args) {
        // Example usage
        String fileName = "example.txt";
        String extension = getFileExtension(fileName);
        System.out.println("File extension: " + extension);
    }
}