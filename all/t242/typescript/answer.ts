function classifyFilesByExtension(fileNames: string[]): {[key: string]: string[]} {
  const classifiedFiles: {[key: string]: string[]} = {};

  for (const file of fileNames) {
      // Split the file name into name and extension
      const parts = file.split('.');
      const name = parts.slice(0, -1).join('.');
      const ext = parts[parts.length - 1] || null;

      // If there is an extension, classify it
      if (ext) {
          const normalizedExt = ext.toLowerCase();  // Normalize the extension to lowercase
          if (!classifiedFiles[normalizedExt]) {
              classifiedFiles[normalizedExt] = [];
          }
          classifiedFiles[normalizedExt].push(file);
      }
  }

  return classifiedFiles;
}