function stringSideBySide(string1, string2, columnWidth = 20) {
  const lines1 = string1.split('\n');
  const lines2 = string2.split('\n');

  const maxLength = Math.max(lines1.length, lines2.length);

  // Pad shorter array with empty strings
  const paddedLines1 = Array.from({ length: maxLength }, (_, i) => lines1[i] || '');
  const paddedLines2 = Array.from({ length: maxLength }, (_, i) => lines2[i] || '');

  // Format and concatenate lines
  const formattedLines = paddedLines1.map((line1, i) => {
    const line2 = paddedLines2[i];
    const formattedLine1 = line1.padEnd(columnWidth, ' ');
    const formattedLine2 = line2.padEnd(columnWidth, ' ');
    return `${formattedLine1} | ${formattedLine2}`;
  });

  // Join all formatted lines into a single string
  return formattedLines.join('\n');
}

// Example usage
console.log(stringSideBySide("Hello\nWorld", "Foo\nBar"));