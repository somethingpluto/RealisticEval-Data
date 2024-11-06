import fs from 'fs'
function extractBibInfo(bibFile) {
    const articles = [];

    // Regular expressions to match title, author, and year
    const titlePattern = /title\s*=\s*{([^}]*)}/i;
    const authorPattern = /author\s*=\s*{([^}]*)}/i;
    const yearPattern = /year\s*=\s*{([^}]*)}/i;

    try {
        const content = fs.readFileSync(bibFile, 'utf8');

        // Split the content into individual entries based on '@'
        const entries = content.split('@').slice(1);  // Skip the first split, which is empty

        for (const entry of entries) {
            const titleMatch = entry.match(titlePattern);
            const authorMatch = entry.match(authorPattern);
            const yearMatch = entry.match(yearPattern);

            // Extracting matched groups if found
            articles.push({
                'title': titleMatch ? titleMatch[1] : null,
                'author': authorMatch ? authorMatch[1] : null,
                'year': yearMatch ? yearMatch[1] : null
            });
        }

    } catch (error) {
        if (error.code === 'ENOENT') {
            console.error(`Error: The file '${bibFile}' was not found.`);
        } else {
            throw error;  // Re-throw the error if it's not a file not found error
        }
    }

    return articles;
}