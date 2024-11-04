function removeCommonIndentation(multilineText: string): string {
    const lines = multilineText.split('\n');
    const nonEmptyLines = lines.filter(line => line.trim().length > 0);
    let minIndent = Infinity;
    for (const line of nonEmptyLines) {
        const strippedLine = line.replace(/^\s+/, '');
        const indent = line.length - strippedLine.length;
        minIndent = Math.min(minIndent, indent);
    }
    if (minIndent === Infinity) {
        return multilineText;
    }
    const sanitizedLines = lines.map(line => line.slice(minIndent));
    return sanitizedLines.join('\n');
}
