describe('parseCategoriesFromSummary', () => {
    test('extracts categories and cleans the summary correctly', () => {
        const input = "This is a summary. Categories: [Technology, Health]";
        const expected = {
            summary: "This is a summary.",
            categories: ["Technology", "Health"]
        };
        expect(parseCategoriesFromSummary(input)).toEqual(expected);
    });

    test('returns empty categories and original summary when no categories are present', () => {
        const input = "This is a summary without categories.";
        const expected = {
            summary: "This is a summary without categories.",
            categories: []
        };
        expect(parseCategoriesFromSummary(input)).toEqual(expected);
    });

    test('ignores case of the category prefix', () => {
        const input = "Summary text. categories: [Education, Science]";
        const expected = {
            summary: "Summary text.",
            categories: ["Education", "Science"]
        };
        expect(parseCategoriesFromSummary(input)).toEqual(expected);
    });

    test('handles extra spaces and malformed category strings correctly', () => {
        const input = "Details follow. Categories: [ Business ,  , Finance]";
        const expected = {
            summary: "Details follow.",
            categories: ["Business", "Finance"]  // Note the removal of an empty string due to extra commas
        };
        expect(parseCategoriesFromSummary(input)).toEqual(expected);
    });

    test('removes the category string correctly even if it appears in the middle of the summary', () => {
        const input = "Beginning of summary. Categories: [Art, Design] Continuation of summary.";
        const expected = {
            summary: "Beginning of summary.  Continuation of summary.",
            categories: ["Art", "Design"]
        };
        expect(parseCategoriesFromSummary(input)).toEqual(expected);
    });
});

/**
 * Extracts categories from a summarized output string and returns the cleaned summary and categories.
 * The categories are expected to be in the format "Categories: [category1, category2, ...]".
 *
 * @param {string} summarizedOutput - The summary text potentially containing categorized data.
 * @returns {object} An object containing the cleaned summary text and an array of categories.
 */
function parseCategoriesFromSummary(summarizedOutput = '') {
    // Define the regex to find the categories pattern in the summary
    const categoriesRegex = /Categories:\s*\[([^\]]+)\]/i;

    // Attempt to match the pattern
    const match = summarizedOutput.match(categoriesRegex);

    let categories = [];
    let summary = summarizedOutput;

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