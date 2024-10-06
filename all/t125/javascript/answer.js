function compressHTML(html) {
    // Remove leading/trailing whitespace around tags
    html = html.replace(/\s*(<[^>]+>)\s*/g, '\$1');
    // Remove multiple newlines and replace with a single space
    html = html.replace(/\n+/g, ' ');
    // Remove multiple spaces and replace them with a single space
    html = html.replace(/[ \t]+/g, ' ');
    return html.trim();
}