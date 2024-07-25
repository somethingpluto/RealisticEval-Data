function getCSSFromSheet(sheet) {
    return Array.from(sheet.cssRules)
        .map((rule) => rule.cssText)
        .join("");
}