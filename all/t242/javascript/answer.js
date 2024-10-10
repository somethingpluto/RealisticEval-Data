function classifyFilesByExtension(fileNames) {
  const classifiedFiles = {};

  for (const fileName of fileNames) {
    const extension = fileName.split('.').pop();

    if (!classifiedFiles[extension]) {
      classifiedFiles[extension] = [];
    }

    classifiedFiles[extension].push(fileName);
  }

  return classifiedFiles;
}