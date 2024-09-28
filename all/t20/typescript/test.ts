// Assume the function is defined in a module file named "markdown.ts"
export function processMarkdown(s: string): string {
    if ((s.match(/\*/g) || []).length <= 2) {
        return s;
    }
    const firstStarIndex = s.indexOf('*');
    const lastStarIndex = s.lastIndexOf('*');
    return s.slice(0, firstStarIndex + 1) + s.slice(firstStarIndex + 1, lastStarIndex).replace(/\*/g, '') + s.slice(lastStarIndex);
}