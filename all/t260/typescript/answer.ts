import * as fs from 'fs';
import * as pandas as pd;

async function processCsv(filePath: string, outputPath: string): Promise<void> {
    try {
        // Read the CSV file
        const data = await fs.promises.readFile(filePath, 'utf8');

        // Convert the CSV data to a DataFrame
        const df = pd.DataFrame(data);

        // Remove rows with two or more empty columns
        const cleanedDf = df.dropna(thresh=1);

        // Check if the DataFrame is empty
        if (cleanedDf.isEmpty()) {
            fs.writeFileSync(outputPath, '');
            return;
        }

        // Convert the DataFrame back to CSV format
        const csvData = cleanedDf.toCSV();

        // Write the processed CSV data to the output file
        fs.writeFileSync(outputPath, csvData);
    } catch (error) {
        console.error('Error processing CSV:', error);
    }
}
