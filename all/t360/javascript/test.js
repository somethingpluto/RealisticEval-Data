describe("getLastPartOfFilepath Test Cases", () => {
    // Test Case 1: Unix-style path with '/'
    test("should return 'file.txt' for Unix-style path", () => {
        expect(getLastPartOfFilepath("/home/user/documents/file.txt")).toBe("file.txt");
    });

    // Test Case 2: Windows-style path with '\\'
    test("should return 'file.txt' for Windows-style path", () => {
        expect(getLastPartOfFilepath("C:\\Users\\JohnDoe\\Documents\\file.txt")).toBe("file.txt");
    });

    // Test Case 3: Path without any separators (should return the original string)
    test("should return original string 'file.txt' if no separators are present", () => {
        expect(getLastPartOfFilepath("file.txt")).toBe("file.txt");
    });

    // Test Case 4: Path ending with a separator (should return an empty string)
    test("should return an empty string for path ending with a separator", () => {
        expect(getLastPartOfFilepath("/home/user/documents/")).toBe("");
    });

    // Test Case 5: Path with mixed separators (should return the last part after the last separator)
    test("should return 'file.txt' for path with mixed separators", () => {
        expect(getLastPartOfFilepath("C:/Users\\JohnDoe/Documents/file.txt")).toBe("file.txt");
    });
});