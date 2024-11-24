function saveContentToFile(content, path) {
    const lines = content.split('\n').filter(line => line.trim().length > 0).map(line => line.trim());
    content = lines.join('\n');

    // Replace multiple spaces with a single space.
    content = content.replace(/\s+/g, ' ');

    // Write the cleaned content to the specified file.
    const fs = require('fs');
    fs.writeFileSync(path, content, { encoding: 'utf-8' });
}
