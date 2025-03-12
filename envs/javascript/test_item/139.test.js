/**
 * Extracts categories from a summarized output string and returns the cleaned summary and categories.
 * The categories are expected to be in the format "Categories: [category1, category2, ...]".
 *
 * @param {string} summarizedOutput - The summary text potentially containing categorized question.
 * @returns {object} An object containing the cleaned summary text and an array of categories.
 */
function parseCategoriesFromSummary(summarizedOutput = '') {
    // Initialize the result object
    const result = {
        cleanedSummary: summarizedOutput,
        categories: []
    };

    // Define the regex pattern to match the categories section
    const categoriesPattern = /Categories:\s*\[([^\]]+)\]/;

    // Execute the regex on the summarized output
    const match = summarizedOutput.match(categoriesPattern);

    // If a match is found, extract the categories
    if (match) {
        // Extract the categories string from the match
        const categoriesString = match[1];

        // Split the categories string into an array
        result.categories = categoriesString.split(',').map(category => category.trim());

        // Remove the categories section from the summarized output
        result.cleanedSummary = summarizedOutput.replace(match[0], '').trim();
    }

    return result;
}
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
            summary: "Beginning of summary. Continuation of summary.",
            categories: ["Art", "Design"]
        };
        expect(parseCategoriesFromSummary(input)).toEqual(expected);
    });
});

