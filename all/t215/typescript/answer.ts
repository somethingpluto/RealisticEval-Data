function replaceWordsInFile(filePath: string, replacementDict: {[key: string]: string}): string {
    // read the file content here
    let fs = require('fs');
    let data = fs.readFileSync(filePath, 'utf8');

    // replace words using the dictionary
    for(let key in replacementDict){
        let regex = new RegExp(key, "g");
        data = data.replace(regex, replacementDict[key]);
    }

    return data;
}