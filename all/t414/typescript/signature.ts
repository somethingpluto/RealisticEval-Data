/**
 * Extracts the title, author, and year from a BibTeX file.
 * 
 * Example of bibtex file content:
 * @article{sample2024,
 *   author = {John Doe and Jane Smith},
 *   title = {A Comprehensive Study on AI},
 *   year = {2024}
 * }
 *
 * @param bibFile - The path to the BibTeX file.
 * @returns An array of objects containing title, author, and year for each article.
 */
function extractBibInfo(bibFile: string): Array<{title: string, author: string, year: string}> {}