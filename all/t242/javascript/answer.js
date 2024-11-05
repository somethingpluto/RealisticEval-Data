function classifyFilesByExtension(fileNames) {
  /**
   * Classify an array of file names according to their file extensions.
   *
   * @param {string[]} fileNames - List of file names.
   * @returns {Object} - Dictionary with file extensions as keys and lists of file names as values.
   */
  const classifiedFiles = {};

  for (const file of fileNames) {
      // Split the file name into name and extension
      const parts = file.split('.');
      const name = parts.slice(0, -1).join('.');
      const ext = parts[parts.length - 1];

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