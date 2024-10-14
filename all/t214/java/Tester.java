public class Tester {

    @Test
    void testValidMappingFile() throws IOException {
        // Test with a valid mapping file content
        String mockFileContent = "'old_pattern1','new_word1'\n'old_pattern2','new_word2'\n";
        File tempFile = File.createTempFile("dummy", ".txt");
        try (FileWriter writer = new FileWriter(tempFile)) {
            writer.write(mockFileContent);
        }

        List<Tuple<Pattern, String>> result = readMappingFile(tempFile.getAbsolutePath());
        List<Tuple<Pattern, String>> expected = List.of(
            new Tuple<>(Pattern.compile("old_pattern1"), "new_word1"),
            new Tuple<>(Pattern.compile("old_pattern2"), "new_word2")
        );

        assertEquals(expected, result);
    }

    @Test
    void testMissingFile() {
        // Test with a missing file
        assertThrows(IOException.class, () -> readMappingFile("non_existent_file.txt"));
    }

    @Test
    void testMalformedLineNoComma() throws IOException {
        // Test with a line that does not contain a comma
        String mockFileContent = "'old_pattern1' 'new_word1'\n";
        File tempFile = File.createTempFile("dummy", ".txt");
        try (FileWriter writer = new FileWriter(tempFile)) {
            writer.write(mockFileContent);
        }

        assertThrows(IllegalArgumentException.class, () -> readMappingFile(tempFile.getAbsolutePath()));
    }

    @Test
    void testValidPatternsWithSpecialCharacters() throws IOException {
        // Test with valid patterns that contain special regex characters
        String mockFileContent = "'\\d+', 'number'\n'\\w+', 'word'\n";
        File tempFile = File.createTempFile("dummy", ".txt");
        try (FileWriter writer = new FileWriter(tempFile)) {
            writer.write(mockFileContent);
        }

        List<Tuple<Pattern, String>> result = readMappingFile(tempFile.getAbsolutePath());
        List<Tuple<Pattern, String>> expected = List.of(
            new Tuple<>(Pattern.compile("\\d+"), "number"),
            new Tuple<>(Pattern.compile("\\w+"), "word")
        );

        assertEquals(expected, result);
    }
}