/**
 * Reads a log file containing JSON entries and extracts training loss and test accuracy.
 * JSON entries such as {"test_acc1": 88.5, "train_loss": 0.75}.
 * 
 * @param {string} logFilePath - The path to the log file to be read.
 * @returns {Array} A tuple containing two lists:
 *   - trainLossList (Array): A list of training loss values extracted from the log.
 *   - testAcc1List (Array): A list of test accuracy values extracted from the log.
 */
function readLog(logFilePath) {
    const trainLossList = [];
    const testAcc1List = [];

    // Read the file and parse each line as JSON
    const fs = require('fs');
    const logData = fs.readFileSync(logFilePath, 'utf8').split('\n');

    logData.forEach(line => {
        const logEntry = JSON.parse(line);
        if ('train_loss' in logEntry) {
            trainLossList.push(logEntry.train_loss);
        }
        if ('test_acc1' in logEntry) {
            testAcc1List.push(logEntry.test_acc1);
        }
    });

    return [trainLossList, testAcc1List];
}
const fs = require('fs');
const { mock } = require('jest-mock-extended');
describe('TestReadLog', () => {
    it('test_read_correct_data', () => {
        const mockFileContent = '{"test_acc1": 88.5, "train_loss": 0.75}\n{"test_acc1": 89.0, "train_loss": 0.70}';
        const mockFs = mock(fs);
        mockFs.readFileSync.mockReturnValue(mockFileContent);

        const [trainLoss, testAcc1] = readLog('dummy_path.json');
        expect(trainLoss).toEqual([0.75, 0.70]);
        expect(testAcc1).toEqual([88.5, 89.0]);
    });

    it('test_read_correct_data_single', () => {
        const mockFileContent = '{"test_acc1": 88.5, "train_loss": 0.75}';
        const mockFs = mock(fs);
        mockFs.readFileSync.mockReturnValue(mockFileContent);

        const [trainLoss, testAcc1] = readLog('dummy_path.json');
        expect(trainLoss).toEqual([0.75]);
        expect(testAcc1).toEqual([88.5]);
    });

    it('test_empty_file', () => {
        const mockFileContent = '';
        const mockFs = mock(fs);
        mockFs.readFileSync.mockReturnValue(mockFileContent);

        const [trainLoss, testAcc1] = readLog('empty_file.json');
        expect(trainLoss).toEqual([]);
        expect(testAcc1).toEqual([]);
    });

    it('test_partial_data_entries', () => {
        const mockFileContent = '{"test_acc1": 88.5, "train_loss": 0.75}\n{"test_acc1": 90.0,"train_loss": 0.75,"f1":0.91}';
        const mockFs = mock(fs);
        mockFs.readFileSync.mockReturnValue(mockFileContent);

        const [trainLoss, testAcc1] = readLog('partial_data_file.json');
        expect(trainLoss).toEqual([0.75, 0.75]);
        expect(testAcc1).toEqual([88.5, 90.0]);
    });
});
