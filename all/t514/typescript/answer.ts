import * as re from 'xregexp';

function extractDateFromFileName(fileName: string): string | null {
    /**
     * Extracts the date in the format YYYY-MM-DD from the given file name.
     *
     * @param fileName - The name of the file which may contain a date.
     * @returns The extracted date string in YYYY-MM-DD format if found, else null.
     */
    // Define the regex pattern for matching a date in the format YYYY-MM-DD
    const datePattern = '\\d{4}-\\d{2}-\\d{2}';

    // Search for the date pattern in the file name
    const match = re.exec(fileName, new RegExp(datePattern));

    // If a match is found, return the matched date; otherwise, return null
    return match ? match[0] : null;
}