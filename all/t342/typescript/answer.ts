/**
 * Parses markdown text to extract titles of different levels.
 *
 * This function takes a string of markdown content as input and returns an
 * object containing arrays of titles categorized by their level:
 * level 1 (H1), level 2 (H2), and level 3 (H3).
 *
 * @param markdown - A string containing markdown formatted text.
 * @returns An object with three properties: level1, level2, and level3,
 *          each holding an array of corresponding titles found in the markdown.
 */
function parseMarkdownTitles(markdown) {
    // Initialize an object to store titles categorized by their levels.
    const result = {
        level1: [], // Array to store level 1 titles (H1)
        level2: [], // Array to store level 2 titles (H2)
        level3: []  // Array to store level 3 titles (H3)
    };

    // Split the input markdown text into individual lines.
    const lines = markdown.split('\n');

    // Iterate through each line in the markdown content.
    lines.forEach(line => {
        line = line.trim(); // Remove leading and trailing whitespace from the line.

        // Check if the line starts with a level 1 markdown header (#).
        if (line.startsWith('# ')) {
            // Extract the title after the header and push it to level1 array.
            result.level1.push(line.slice(2)); // Remove the '# ' prefix.

            // Check if the line starts with a level 2 markdown header (##).
        } else if (line.startsWith('## ')) {
            // Extract the title after the header and push it to level2 array.
            result.level2.push(line.slice(3)); // Remove the '## ' prefix.

            // Check if the line starts with a level 3 markdown header (###).
        } else if (line.startsWith('### ')) {
            // Extract the title after the header and push it to level3 array.
            result.level3.push(line.slice(4)); // Remove the '### ' prefix.
        }
    });

    // Return the object containing categorized titles.
    return result;
}
