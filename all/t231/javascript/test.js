describe('readLog function', () => {
    it('should extract training loss and test accuracy from a valid log file', () => {
        const logFilePath = path.join(__dirname, 'example.log'); // Replace with actual log file path
        const expectedTrainLossList = [0.75]; // Replace with expected training loss values
        const expectedTestAcc1List = [88.5]; // Replace with expected test accuracy values

        const [trainLossList, testAcc1List] = readLog(logFilePath);

        expect(trainLossList).toEqual(expectedTrainLossList);
        expect(testAcc1List).toEqual(expectedTestAcc1List);
    });

    it('should handle empty or invalid log files gracefully', () => {
        const logFilePath = path.join(__dirname, 'empty.log'); // Replace with actual log file path
        const [trainLossList, testAcc1List] = readLog(logFilePath);

        expect(trainLossList).toEqual([]);
        expect(testAcc1List).toEqual([]);
    });
});