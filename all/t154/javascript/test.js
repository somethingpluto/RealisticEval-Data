describe('parseGitDiff', () => {

    test('should parse a simple file addition', () => {
        const diffText = `diff --git a/file.txt b/file.txt
new file mode 100644
index 0000000..e69de29
--- /dev/null
+++ b/file.txt`;
        // @ts-ignore
        const result = parseGitDiff(diffText);
        expect(result).toHaveLength(1);
        expect(result[0].oldPath).toBe('file.txt');
        expect(result[0].newPath).toBe('file.txt');
        expect(result[0].newFileMode).toBe('100644');
    });

    test('should parse a simple file deletion', () => {
        const diffText = `diff --git a/file.txt b/file.txt
deleted file mode 100644
index e69de29..0000000
--- a/file.txt
+++ /dev/null`;
        // @ts-ignore
        const result = parseGitDiff(diffText);
        expect(result).toHaveLength(1);
        expect(result[0].oldPath).toBe('file.txt');
        expect(result[0].newPath).toBe('file.txt');
        expect(result[0].deletedFileMode).toBe('100644');
    });

    test('should parse a file modification with changes', () => {
        const diffText = `diff --git a/file.txt b/file.txt
index e69de29..d95f3ad 100644
--- a/file.txt
+++ b/file.txt
@@ -0,0 +1 @@
+Hello World`;

        // @ts-ignore
        const result = parseGitDiff(diffText);

        expect(result).toHaveLength(1); // Ensure only one file diff is parsed
        expect(result[0].oldPath).toBe('file.txt'); // Validate old file path
        expect(result[0].newPath).toBe('file.txt'); // Validate new file path
        expect(result[0].index).toBe('e69de29..d95f3ad'); // Validate index value
        expect(result[0].changes).toEqual([
            { code: "--- a/file.txt" }, // Validate old file path line
            { code: "+++ b/file.txt" }, // Validate new file path line
            { diff: '@@ -0,0 +1 @@' },  // Validate diff header
            { code: '+Hello World' }     // Validate code addition
        ]); // Validate changes array
    });

    test('should handle multiple file diffs', () => {
        const diffText = `diff --git a/file1.txt b/file1.txt
index e69de29..d95f3ad 100644
--- a/file1.txt
+++ b/file1.txt
@@ -0,0 +1 @@
+Hello World
diff --git a/file2.txt b/file2.txt
index 0a1b2c3..d4e5f6a 100644
--- a/file2.txt
+++ b/file2.txt
@@ -1 +1 @@
-Hello
+Hi`;
        // @ts-ignore
        const result = parseGitDiff(diffText);
        expect(result).toHaveLength(2);
        expect(result[0].oldPath).toBe('file1.txt');
        expect(result[1].oldPath).toBe('file2.txt');
    });

    test('should return an empty array for empty diff text', () => {
        // @ts-ignore
        const result = parseGitDiff('');
        expect(result).toEqual([]);
    });

});