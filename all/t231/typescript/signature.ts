/**
 * Reads a log file containing JSON entries and extracts training loss and test accuracy.
 * Json entries such as {"test_acc1": 88.5, "train_loss": 0.75}
 *
 * @param logFilePath - The path to the log file to be read.
 * @returns A tuple containing two arrays:
 *          - trainLossList: An array of training loss values extracted from the log.
 *          - testAcc1List: An array of test accuracy values extracted from the log.
 */
function readLog(logFilePath: string): [number[], number[]] {}