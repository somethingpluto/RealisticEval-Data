function formatText(inputFile: string = 'input.txt', outputFile: string = 'output.txt'): void {
    try {
        // Open the input file in read mode
        const fs = require('fs').promises;
        const content = fs.readFile(inputFile, 'utf8');

        // Read the content of the input file line by line
        content.then((data) => {
            const lines = data.split('\n');

            // Process each line
            const processedLines: string[] = [];
            for (const line of lines) {
                // Remove newline characters and add a space
                const processedLine = line.trimEnd();
                processedLines.push(processedLine);  // Append the processed line
            }

            // Join the processed lines with spaces
            const contentWithoutNewlines = processedLines.join(' ');

            // Open the output file in write mode
            fs.writeFile(outputFile, contentWithoutNewlines)
                .then(() => {
                    console.log("Line breaks removed and spaces added. Output written to", outputFile);
                })
                .catch((error) => {
                    console.error("Error writing to output file:", error);
                });
        })
        .catch((error) => {
            if (error.code === 'ENOENT') {
                console.error("Input file not found.");
            } else {
                console.error("Error reading input file:", error);
            }
        });
    } catch (error) {
        console.error("An unexpected error occurred:", error);
    }
}