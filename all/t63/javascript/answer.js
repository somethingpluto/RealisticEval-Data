const fs = require('fs');

function dataframeToMarkdown(data, mdPath) {
    // Construct the header row
    const headers = "| " + Object.keys(data[0]).join(" | ") + " |\n";
    
    // Construct the separator row
    const separators = "| " + ("--- | ".repeat(Object.keys(data[0]).length)).slice(0, -3) + " |\n";
    
    // Combine headers and separators
    let markdown = headers + separators;

    // Build markdown table body
    data.forEach(row => {
        markdown += "| " + Object.values(row).map(value => String(value)).join(" | ") + " |\n";
    });

    // Write markdown to file
    fs.writeFile(mdPath, markdown, (err) => {
        if (err) throw err;
        console.log(`Markdown table has been written to ${mdPath}`);
    });

    return markdown;
}