import { DataFrame } from 'pandas-js';

interface DataFrameToMarkdownOptions {
    df: DataFrame;
    mdPath: string;
}

function dataframeToMarkdown({ df, mdPath }: DataFrameToMarkdownOptions): string {

    // Convert DataFrame to Markdown
    const columns = df.columns.map(col => `| ${col} |`).join('\n');
    const separator = '|'.padEnd(columns.length, '-');
    const rows = df.values.map(row => row.map(cell => `| ${cell} |`).join('')).join('\n');

    const markdownContent = `${columns}\n${separator}\n${rows}`;

    // Optionally, write the markdown content to a file if needed
    // fs.writeFileSync(mdPath, markdownContent);

    return markdownContent;
}