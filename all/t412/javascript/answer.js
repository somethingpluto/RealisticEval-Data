function formatText(inputFile = 'input.txt', outputFile = 'output.txt') {
    try {
        // Open the input file in read mode
        const fs = require('fs').promises;
        
        fs.readFile(inputFile, 'utf8')
            .then(data => {
                // Split the content of the input file line by line
                const lines = data.split('\n');

                // Process each line
                const processedLines = lines.map(line => line.trim());

                // Join the processed lines with spaces
                const contentWithoutNewlines = processedLines.join(' ');

                // Open the output file in write mode
                return fs.writeFile(outputFile, contentWithoutNewlines);
            })
            .then(() => {
                console.log("Line breaks removed and spaces added. Output written to", outputFile);
            })
            .catch(error => {
                if (error.code === 'ENOENT') {
                    console.log("Input file not found.");
                } else {
                    throw error;
                }
            });
    } catch (error) {
        console.error(error);
    }
}