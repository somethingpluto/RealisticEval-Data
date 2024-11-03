import * as fs from 'fs';

function findAndReplaceInFile(filePath: string, searchString: string, replaceString: string): void {
    try {
        // Read the content of the file
        const fileContent: string = fs.readFileSync(filePath, 'utf-8');

        // Replace the search string with the replacement string
        const replacedContent: string = fileContent.replace(new RegExp(searchString, 'g'), replaceString);

        // Write the replaced content back to the file
        fs.writeFileSync(filePath, replacedContent, 'utf-8');
    } catch (error) {
        console.error(`Error occurred: ${error}`);
    }
}