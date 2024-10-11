import * as fs from 'fs';
import * as path from 'path';

interface BibEntry {
    title: string;
    author: string;
    year: string;
}

function extractBibInfo(bibFile: string): BibEntry[] {
    /**
     * Extracts the title, author, and year from a BibTeX file.
     *
     * @param {string} bibFile - The path to the BibTeX file.
     * @returns {BibEntry[]} - A list containing dictionaries with title, author, and year for each article.
     */
    
    // Read the content of the BibTeX file
    const fileContent = fs.readFileSync(bibFile, 'utf-8');
    
    // Split the content into individual entries based on '@'
    const entries = fileContent.split('@').filter(entry => entry.trim() !== '');
    
    const results: BibEntry[] = [];
    
    for (const entry of entries) {
        // Find the type of entry (e.g., article, book)
        const entryTypeMatch = entry.match(/^\s*([a-zA-Z]+)\{/);
        if (!entryTypeMatch) continue;
        
        const entryType = entryTypeMatch[1];
        
        // Extract the title, author, and year
        const fields = entry.split(',').map(field => field.trim());
        let title = '', author = '', year = '';
        
        for (const field of fields) {
            const [key, value] = field.split('=').map(part => part.trim().replace(/^{/, '').replace(/}$/, '').trim());
            if (key === 'title') title = value;
            else if (key === 'author') author = value;
            else if (key === 'year') year = value;
        }
        
        results.push({ title, author, year });
    }
    
    return results;
}