
        if (line.startsWith('diff --git a/')) {
            if (currentFile) {
                fileDiffs.push(currentFile);
            }

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
            currentFile.newFileMode = line.split(' ')[3];
        } else if (line.startsWith('deleted file mode')) {
            currentFile.deletedFileMode = line.split(' ')[3];
        } else if (line.startsWith('index')) {
            currentFile.index = line.split(' ')[1];
        } else if (line.startsWith('@@')) {
            currentFile.changes.push({diff: line});
        } else if (
            currentFile &&
            (line.startsWith('+') || line.startsWith('-') || line.startsWith(' '))
        ) {
            currentFile.changes.push({code: line});

        fileDiffs.push(currentFile);

}