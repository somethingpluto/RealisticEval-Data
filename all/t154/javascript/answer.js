function parseGitDiff(diffText) {
    const diffLines = diffText.split('\n');
    const fileDiffs = [];
    let currentFile = null;

    diffLines.forEach((line) => {
        if (line.startsWith('diff --git a/')) {
            // When a new file diff starts, push the current file diff to the array
            if (currentFile) {
                fileDiffs.push(currentFile);
            }

            // Extract the old and new paths from the diff line
            const paths = line.split(' ').slice(2);
            const oldPath = paths[0].substring(2); // Removing 'a/'
            const newPath = paths[1].substring(2); // Removing 'b/'

            currentFile = {
                oldPath: oldPath,
                newPath: newPath,
                changes: [],
                newFileMode: null,
                deletedFileMode: null,
                index: null,
            };
        } else if (line.startsWith('new file mode')) {
            if (currentFile) {
                currentFile.newFileMode = line.split(' ')[3];
            }
        } else if (line.startsWith('deleted file mode')) {
            if (currentFile) {
                currentFile.deletedFileMode = line.split(' ')[3];
            }
        } else if (line.startsWith('index')) {
            if (currentFile) {
                currentFile.index = line.split(' ')[1];
            }
        } else if (line.startsWith('@@')) {
            // Start of a hunk; add it to the changes array
            if (currentFile) {
                currentFile.changes.push({ diff: line });
            }
        } else if (currentFile && (line.startsWith('+') || line.startsWith('-') || line.startsWith(' '))) {
            // Line additions, deletions, or context
            currentFile.changes.push({ code: line });
        }
    });

    // Push the last file diff after the loop ends
    if (currentFile) {
        fileDiffs.push(currentFile);
    }

    return fileDiffs;
}