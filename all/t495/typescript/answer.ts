function filterContentWithContext(
  content: string,
  keywords: string[],
  linesBefore: number = 1,
  linesAfter: number = 1
): string {
  const lines = content.split('\n');
  const matchedLines = new Set<number>();  // Use a Set to avoid duplicate lines

  // Iterate over each line to find matches
  for (let i = 0; i < lines.length; i++) {
      const line = lines[i];
      for (const keyword of keywords) {
          // Use a regular expression to find whole word matches with exact case
          if (new RegExp(`\\b${escapeRegExp(keyword)}\\b`).test(line)) {
              // Determine the range of lines to include for context
              const contextRange = Array.from(
                  { length: linesAfter + linesBefore + 1 }, 
                  (_, k) => Math.max(0, i + k - linesBefore)
              )
              .filter(index => index < lines.length);
              
              contextRange.forEach(index => matchedLines.add(index));  // Add the context lines to the set
          }
      }
  }

  // Extract the matched lines and their context, sorted by their original order
  const filteredLines = Array.from(matchedLines).sort((a, b) => a - b).map(i => lines[i]);

  // Join the filtered lines back into a single string
  const filteredContent = filteredLines.join('\n');

  return filteredContent;
}

// Helper function to escape special characters for regular expressions
function escapeRegExp(string: string): string {
  return string.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}
