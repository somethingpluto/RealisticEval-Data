/**
 * Add a CSS rule to the HTML document to highlight search results
 */
function checkCSSHighlightAndAdd() {
    // Check if the CSS rule already exists
    if (!cssRuleExistsForHighlight) {
        console.log("CSS rule not found, adding it now");

        // Create a new style element
        const style = document.createElement('style');
        // Set the text content of the style element with the CSS rule
        style.textContent = `
        ::highlight(search-result-highlight) {
            background-color: yellow;
            color: black;
        }`;

        // Append the style element to the document head
        document.head.appendChild(style);

        // Update the flag to indicate that the CSS rule now exists
        cssRuleExistsForHighlight = true;
    }
}
