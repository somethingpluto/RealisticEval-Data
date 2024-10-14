/**
 * Extracts categories from a summarized output string and returns the cleaned summary and categories.
 * The categories are expected to be in the format "Categories: [category1, category2, ...]".
 *
 * @param {string} summarizedOutput - The summary text potentially containing categorized question.
 * @returns {object} An object containing the cleaned summary text and an array of categories.
 */
function parseCategoriesFromSummary(summarizedOutput: string = ''): { summary: string; categories: string[] } {
    // Define the regex to find the categories pattern in the summary
    const categoriesRegex = /Categories:\s*\[([^\]]+)\]/i;

    // Attempt to match the pattern
    const match = summarizedOutput.match(categoriesRegex);

    let categories: string[] = [];
    let summary: string = summarizedOutput;

    // If a match is found, process the categories and clean the summary
    if (match && match[1]) {
        categories = match[1].split(',')
            .map(category => category.trim()) // Trim whitespace around categories
            .filter(category => category !== ''); // Remove any empty categories due to malformed strings

        // Remove the category line from the summary and trim any leading/trailing whitespace
        summary = summarizedOutput.replace(categoriesRegex, '').trim();
    }

    return { summary, categories };
}