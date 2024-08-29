interface MarkdownTitleExtractResult {
  title: string;
  sub: MarkdownTitleExtractResult[];
}
function parseMarkdownTitles(markdown: string): MarkdownTitleExtractResult[] {
  const lines = markdown.split('\n').filter(line => line.trim() !== '');
  const titles: MarkdownTitleExtractResult[] = [];
  const currentContext: (MarkdownTitleExtractResult | null)[] = [null, null, null, null];

  lines.forEach(line => {
    line = line.trim();
    const match = line.match(/^(#{1,4}) (.*)/);

    if (match) {
      const level = match[1].length; // Level is determined by the number of '#'
      const title = { title: match[2], sub: [] };

      if (level === 1) {
        titles.push(title);
      } else {
        // Find the nearest upper-level context
        for (let i = level - 2; i >= 0; i--) {
          if (currentContext[i]) {
            currentContext[i]!.sub.push(title);
            break;
          }
        }
      }

      // Update the current context for this level and clear deeper levels
      currentContext[level - 1] = title;
      currentContext.fill(null, level); // Clear all deeper contexts
    }
  });

  return titles;
}