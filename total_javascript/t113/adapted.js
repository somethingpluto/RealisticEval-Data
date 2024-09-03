function getCSSFromSheet(sheet) {
    // Check if the sheet is a valid CSSStyleSheet and has rules we can access
    if (!(sheet instanceof CSSStyleSheet) || !sheet.cssRules) {
        return '';
    }

    // Use Array.from to convert the CSSRuleList into an array and then map and join to construct the final CSS string
    return Array.from(sheet.cssRules)
        .map(rule => rule.cssText)
        .join('');
}
