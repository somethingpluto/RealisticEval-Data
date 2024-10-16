/**
 * Compresses long filenames to the specified maximum length by inserting an ellipsis in the middle while preserving the filename extension, which defaults to 18 characters.
 * For example:
 *      compressFileName("verylongfilename.txt", 10) output: "verylongfi***.txt"
 *
 * @param fileName - The original file name to be compressed.
 * @param maxLength - The maximum allowed length for the compressed file name. Defaults to 18.
 * @return The compressed file name, with the middle section replaced by ellipses ('...'), or the original file name if it is within the maximum length.
 */
public static String compressFileName(String fileName, int maxLength) {}