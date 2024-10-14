describe('parseCategoriesFromSummary', () => {
    test('extracts categories and cleans the summary correctly', () => {
        const input: string = "This is a summary. Categories: [Technology, Health]";
        const expected = {
            summary: "This is a summary.",
            categories: ["Technology", "Health"]
        };
        expect(parseCategoriesFromSummary(input)).toEqual(expected);
    });

    test('returns empty categories and original summary when no categories are present', () => {
        const input: string = "This is a summary without categories.";
        const expected = {
            summary: "This is a summary without categories.",
            categories: []
        };
        expect(parseCategoriesFromSummary(input)).toEqual(expected);
    });

    test('ignores case of the category prefix', () => {
        const input: string = "Summary text. categories: [Education, Science]";
        const expected = {
            summary: "Summary text.",
            categories: ["Education", "Science"]
        };
        expect(parseCategoriesFromSummary(input)).toEqual(expected);
    });

    test('handles extra spaces and malformed category strings correctly', () => {
        const input: string = "Details follow. Categories: [ Business ,  , Finance]";
        const expected = {
            summary: "Details follow.",
            categories: ["Business", "Finance"]  // Note the removal of an empty string due to extra commas
        };
        expect(parseCategoriesFromSummary(input)).toEqual(expected);
    });

    test('removes the category string correctly even if it appears in the middle of the summary', () => {
        const input: string = "Beginning of summary. Categories: [Art, Design] Continuation of summary.";
        const expected = {
            summary: "Beginning of summary. Continuation of summary.",
            categories: ["Art", "Design"]
        };
        expect(parseCategoriesFromSummary(input)).toEqual(expected);
    });
});