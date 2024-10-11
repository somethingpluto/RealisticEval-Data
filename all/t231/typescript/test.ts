describe('read_log', () => {
  it('should return empty arrays when the log file is empty', async () => {
    const logFilePath = 'path/to/empty/logfile.log';
    const [trainLossList, testAcc1List] = await read_log(logFilePath);
    expect(trainLossList).toEqual([]);
    expect(testAcc1List).toEqual([]);
  });

  it('should correctly extract training loss and test accuracy from the log file', async () => {
    const logFilePath = 'path/to/logfile.log'; // Adjust the path to your actual log file
    const [trainLossList, testAcc1List] = await read_log(logFilePath);

    // Assuming the log file contains at least one entry like {"test_acc1": 88.5, "train_loss": 0.75}
    expect(trainLossList).toContain(0.75);
    expect(testAcc1List).toContain(88.5);
  });
});