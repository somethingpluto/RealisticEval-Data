public class FileUtils {
    public static String removeFileExtension(String fileName) {
        // Find the index of the last dot in the file name
        int lastDotIndex = fileName.lastIndexOf('.');

        // If a dot is found and it is not the first character
        if (lastDotIndex != -1) {
            // Return the substring from the beginning to the last dot
            return fileName.substring(0, lastDotIndex);
        }

        // Return the original file name if no dot is found
        return fileName;
    }

    public static void main(String[] args) {
        String filename = "example.txt";
        String result = removeFileExtension(filename);
        System.out.println("File name without extension: " + result);
    }
}