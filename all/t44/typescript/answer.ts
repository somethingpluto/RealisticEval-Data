function stringSideBySide(string1: string, string2: string, columnWidth: number = 20): string {
    const lines1 = string1.split("\n");
    const lines2 = string2.split("\n");

    const maxLength = Math.max(lines1.length, lines2.length);

    // Create arrays with the padded lines
    const paddedLines1 = Array.from({ length: maxLength }, (_, i) =>
        i < lines1.length ? lines1[i] : ""
    );
    const paddedLines2 = Array.from({ length: maxLength }, (_, i) =>
        i < lines2.length ? lines2[i] : ""
    );

    // Format and concatenate lines
    const formattedLines = paddedLines1.map((line1, i) => {
        const line2 = paddedLines2[i];
        return `${line1.padEnd(columnWidth)} | ${line2.padEnd(columnWidth)}`;
    });

    // Join all formatted lines into a single string
    return formattedLines.join("\n");
}

// Example usage
const result = stringSideBySide("Hello\nWorld", "Side\nBy\nSide");
console.log(result);