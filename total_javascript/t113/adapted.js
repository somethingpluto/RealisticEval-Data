/**
 * Extracts and concatenates all CSS rules from a provided stylesheet.
 * @param {CSSStyleSheet} sheet - The stylesheet object from which CSS rules are extracted.
 * @returns {string} A string containing all CSS rules concatenated together.
 */
function getCSSFromSheet(sheet) {
    // Check if the sheet is a valid CSSStyleSheet object
    if (!(sheet instanceof CSSStyleSheet)) {
        throw new TypeError("The provided input is not a valid CSSStyleSheet object.");
    }

    try {
        // Safely attempt to access and map cssRules to their cssText
        const cssRulesList = sheet.cssRules || [];
        return Array.from(cssRulesList)
            .map(rule => rule.cssText)
            .join("");
    } catch (error) {
        // Log the error and return an indication of failure
        console.error("Failed to read CSS rules from the stylesheet:", error);
        return ""; // Return empty string or handle the error as needed
    }
}