function findPlaceholders(text: string): string[] {
    // Use a regular expression to find placeholders in the specified format
    const placeholders = text.matchAll(/{{\s*([\w]+)\s*}}/g);
    const results: string[] = [];
    for (const match of placeholders) {
        results.push(match[1]);
    }
    return results;
}
