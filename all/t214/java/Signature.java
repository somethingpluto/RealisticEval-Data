/**
 * Reads a mapping file and returns a list of tuples with compiled regex and replacement strings.
 *
 * @param mappingFilePath Path to the file containing regex mappings.
 * @return A list of tuples, where each tuple contains a compiled regex object and a corresponding replacement string.
 * @throws IOException If the mapping file does not exist or cannot be read.
 */
public static class Tuple<T1, T2> {
    private T1 first;
    private T2 second;

    public Tuple(T1 first, T2 second) {
        this.first = first;
        this.second = second;
    }

    public T1 getFirst() {
        return first;
    }

    public T2 getSecond() {
        return second;
    }
}
public static List<Tuple<Pattern, String>> readMappingFile(String mappingFilePath) throws IOException {}