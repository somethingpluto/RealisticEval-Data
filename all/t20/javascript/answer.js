function processMarkdown(s) {
    if ((s.match(/\*/g) || []).length <= 2) {
        return s;
    }
    let firstStarIndex = s.indexOf('*');
    let lastStarIndex = s.lastIndexOf('*');
    return s.slice(0, firstStarIndex + 1) + s.slice(firstStarIndex + 1, lastStarIndex).replace(/\*/g, '') + s.slice(lastStarIndex);
}

// Example Usage:
// console.log(processMarkdown("This *is* a *test* string *with* more *stars*."));