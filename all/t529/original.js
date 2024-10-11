function saveAsJSON(data, outputFilePath) {
    const jsonData = JSON.stringify(data, null, 2)
    fs.writeFileSync(outputFilePath, jsonData, 'utf8')
    }