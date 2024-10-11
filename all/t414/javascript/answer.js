function extractBibInfo(bibFile) {
    /**
     * Extracts the title, author, and year from a BibTeX file.
     *
     * @param {string} bibFile - The path to the BibTeX file.
     *
     * @returns {Array.<Object>} - A list containing objects with title, author, and year for each article.
     */
    
    const data = fs.readFileSync(bibFile, 'utf8');
    const regex = /@article{(.*?),(.*?)=(.*?),(.*?)=(.*?),(.*?)=(.*?)}/g;
    let match;
    let result = [];

    while ((match = regex.exec(data)) !== null) {
        result.push({
            title: match[3],
            author: match[5].replace(/and/g, ',').trim(),
            year: match[7]
        });
    }

    return result;
}