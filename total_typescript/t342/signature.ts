interface MarkdownTitleExtractResult {
    title: string;
    sub: MarkdownTitleExtractResult[];
}

/**
 * parse the titles of the Markdown string and build a hierarchy that contains these titles and their subtitles. The function matches different levels of titles (from #to ####) through regular expressions and stores them in an array. Each matching title is added under the appropriate parent title based on its hierarchy. If the title has no superior title, it will be added directly to the main array
 * @param markdown
 */
function parseMarkdownTitles(markdown: string): MarkdownTitleExtractResult[] {

}