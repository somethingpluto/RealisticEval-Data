function readLog(logFilePath) {
    /*
    Reads a log file containing JSON entries and extracts training loss and test accuracy.
    Json entries such as {"test_acc1": 88.5, "train_loss": 0.75}

    Parameters:
        logFilePath (string): The path to the log file to be read.

    Returns:
        object: An object containing two arrays:
            - trainLossList (array): An array of training loss values extracted from the log.
            - testAcc1List (array): An array of test accuracy values extracted from the log.
    */

    // Assume we have some way to read files in Node.js or use an API in browser
    let fileContent = fs.readFileSync(logFilePath, 'utf-8');
    let jsonEntries = fileContent.split('\n');
    let trainLossList = [];
    let testAcc1List = [];

    for(let entry of jsonEntries){
        if(entry.trim() !== ''){ // Check if it's not just whitespace
            let parsedEntry = JSON.parse(entry);
            trainLossList.push(parsedEntry.train_loss);
            testAcc1List.push(parsedEntry.test_acc1);
        }
    }

    return { trainLossList, testAcc1List };
}