function compareFiles(file1Path, file2Path) {
    try {
        const file1Content = fs.readFileSync(file1Path, 'utf8');
        const file2Content = fs.readFileSync(file2Path, 'utf8');

        // Split the content into lines
        const lines1 = file1Content.split('\n');
        const lines2 = file2Content.split('\n');

        let result = [];

        for(let i = 0; i < Math.max(lines1.length, lines2.length); i++) {
            if (lines1[i] !== lines2[i]) {
                result.push(`-${lines1[i]}`);
                result.push(`+${lines2[i]}`);
            }
        }

        return result;
    } catch (error) {
        console.error(error);
        throw error;
    }
}