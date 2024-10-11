/**
 * Reads a log file containing JSON entries and extracts training loss and test accuracy.
 * Json entries such as {"test_acc1": 88.5, "train_loss": 0.75}
 *
 * @param {string} logFilePath - The path to the log file to be read.
 * @returns {Object} An object containing two arrays:
 * @property {Array<number>} trainLossList - An array of training loss values extracted from the log.
 * @property {Array<number>} testAcc1List - An array of test accuracy values extracted from the log.
 */
function readLog(logFilePath) {}