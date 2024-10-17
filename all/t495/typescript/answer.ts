import { escape, search } from 'regexp';

function filterContentWithContext(
  content: string,
  keywords: string[],
  linesBefore: number = 1,
  linesAfter: number = 1
): string {
  /**
   * Filters website content to include lines containing any of the specified keywords as whole words,
   * along with a specified number of lines before and after for context. This version uses regular expressions
   * to ensure exact, whole word matching and respects case sensitivity.
   *
   * @param content - The full text content of the website.
   * @param keywords - A list of strings to search for within the content.
   * @param linesBefore - Number of lines to include before a matching line.
   * @param linesAfter - Number of lines to include after a matching line.
   *
   * @returns A string containing the filtered content with additional context.
   */

  // Split the content into individual lines
  const lines = content.split('\n');
  const matchedLines = new Set<number>();  // Use a set to avoid duplicate lines

  // Iterate over each line to find matches
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    for (const keyword of keywords) {
      // Use a regular expression to find whole word matches with exact case
      if (search(`\\b${escape(keyword)}\\b`, line)) {
        // Determine the range of lines to include for context
        const contextRange = Array.from({
          length: linesAfter - linesBefore + 1
        }, (_, k) => Math.max(0, i - linesBefore + k)).filter(x => x < lines.length);
        matchedLines.addAll(contextRange);  // Add the context lines to the set
      }
    }
  }

  // Extract the matched lines and their context, sorted by their original order
  const filteredLines = Array.from(matchedLines).sort().map(index => lines[index]);

  // Join the filtered lines back into a single string
  const filteredContent = filteredLines.join('\n');

  return filteredContent;
}

// Helper function to escape special characters
function escape(str: string): string {
  return str.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}

// Helper function to simulate Python's re.search
function search(pattern: string, text: string): boolean {
  const regex = new RegExp(pattern);
  return regex.test(text);
}