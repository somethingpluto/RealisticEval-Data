function convert(html: string): string {
    // Replace line breaks
    let markdown = html.replace(/<br\s*\/?>/gi, '\n');

    // Replace paragraph tags
    markdown = markdown.replace(/<p>/gi, '');
    markdown = markdown.replace(/<\/p>/gi, '\n\n');

    // Replace strong and bold tags
    markdown = markdown.replace(/<strong>/gi, '**');
    markdown = markdown.replace(/<\/strong>/gi, '**');

    // Replace italic tags with emphasis
    markdown = markdown.replace(/<em>/gi, '*');
    markdown = markdown.replace(/<\/em>/gi, '*');

    // Replace underline (not native to markdown, commonly represented with emphasis)
    markdown = markdown.replace(/<u>/gi, '*');
    markdown = markdown.replace(/<\/u>/gi, '*');

    // Replace code tags
    markdown = markdown.replace(/<code>/gi, '`');
    markdown = markdown.replace(/<\/code>/gi, '`');

    // Replace unordered lists
    markdown = markdown.replace(/<ul>/gi, '');
    markdown = markdown.replace(/<\/ul>/gi, '');

    // Replace ordered lists
    markdown = markdown.replace(/<ol>/gi, '');
    markdown = markdown.replace(/<\/ol>/gi, '');

    // Replace list items
    markdown = markdown.replace(/<li>/gi, '* ');
    markdown = markdown.replace(/<\/li>/gi, '\n');

    // Correctly replace anchor tags in one pass
    markdown = markdown.replace(/<a\s+href="([^"]*)">(.*?)<\/a>/gi, '[$2]($1)');

    return markdown;
}