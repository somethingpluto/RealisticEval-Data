/**
 * Reads a text file, replaces words according to a dictionary map, and returns the modified text.
 *
 * @param filePath   the path to the text file
 * @param replacementDict a dictionary where the keys are words to be replaced, and the values are the replacement words
 * @return the text with the words replaced
 */
public String replaceWordsInFile(String filePath, Map<String, String> replacementDict);