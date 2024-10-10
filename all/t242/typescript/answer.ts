interface FileNamesByExtension {
  [key: string]: string[];
}

function classifyFilesByExtension(fileNames: string[]): FileNamesByExtension {
  let result: FileNamesByExtension = {};

  for(let fileName of fileNames) {
    let extension = fileName.split('.').pop();
    if(!result[extension]) {
      result[extension] = [];
    }
    result[extension].push(fileName);
  }

  return result;
}