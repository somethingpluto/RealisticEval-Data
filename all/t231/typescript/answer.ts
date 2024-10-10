interface LogEntry {
    test_acc1?: number;
    train_loss?: number;
}

function readLog(logFilePath: string): [number[], number[]] {
    let trainLossList: number[] = [];
    let testAcc1List: number[] = [];

    try {
        const fs = require('fs');
        const data = fs.readFileSync(logFilePath, 'utf-8');

        const logs = data.split('\n').filter(Boolean);

        for(const log of logs) {
            try {
                const entry: LogEntry = JSON.parse(log);

                if(entry.train_loss !== undefined) {
                    trainLossList.push(entry.train_loss);
                }

                if(entry.test_acc1 !== undefined) {
                    testAcc1List.push(entry.test_acc1);
                }
            } catch(error) {
                console.error(`Error parsing log entry: ${log}`);
            }
        }
    } catch(error) {
        console.error(`Error reading log file: ${error.message}`);
    }

    return [trainLossList, testAcc1List];
}