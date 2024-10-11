const { readCSV, writeCSV } = require('node-pandas');

async function processCSV(filePath, outputPath) {
    try {
        let df = await readCSV(filePath);
        if(df.isEmpty()){
            return '';
        }
        let dfWithoutEmptyColumns = df.dropna({how:'all'});
        await writeCSV(dfWithoutEmptyColumns, outputPath);
    } catch(error) {
        console.error(`Error processing CSV: ${error}`);
    }
}

module.exports = processCSV;