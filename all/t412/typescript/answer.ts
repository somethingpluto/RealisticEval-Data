import * as fs from 'fs';

function formatText(inputFile: string = 'input.txt', outputFile: string = 'output.txt'): void {
    try {
        // Read the content of the input file
        const data: string = fs.readFileSync(inputFile, 'utf8');

        // Process the data to remove newlines and add a space
        const processedContent: string = data.split('\n').map(line => line.trim()).join(' ');

        // Write the processed content to the output file
        fs.writeFileSync(outputFile, processedContent);

        console.log(`Line breaks removed and spaces added. Output written to ${outputFile}`);
    } catch (error) {
        if ((error as NodeJS.ErrnoException).code === 'ENOENT') {
            console.error('Input file not found.');
        } else {
            console.error('An error occurred:', (error as Error).message);
        }
    }
}