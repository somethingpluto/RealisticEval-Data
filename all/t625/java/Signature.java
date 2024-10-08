/**
 * Reads data from a specified file and determines the type of each line.
 * The method processes each line of the file and attempts to convert it
 * into either an integer, a floating-point number, or a string.
 *
 * @param path the path to the file to be read. The file should exist and be accessible for reading.
 *
 * @return a list of Objects where each object can be an Integer, Float, or String,
 *         representing the converted values of each line in the file.
 *
 * @throws IllegalArgumentException if an I/O error occurs while reading the file.
 *         This may happen if the file does not exist, or if the program lacks
 *         permissions to read the file.
 */
public List<Object> readDataFromFile(String path) {}