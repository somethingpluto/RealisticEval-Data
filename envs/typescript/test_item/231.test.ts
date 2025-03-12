import * as fs from 'fs';
import * as path from 'path';
import { promisify } from 'util';
import { parse } from 'json5';

const readFileAsync = promisify(fs.readFile);

async function readLog(logFilePath: string): Promise<[number[], number[]]> {
  try {
    const content = await readFileAsync(logFilePath, 'utf8');
    const logEntries = parse(content);
    const trainLossList: number[] = [];
    const testAcc1List: number[] = [];

    for (const entry of logEntries) {
      if (entry.hasOwnProperty('train_loss') && entry.hasOwnProperty('test_acc1')) {
        trainLossList.push(parseFloat(entry['train_loss']));
        testAcc1List.push(parseFloat(entry['test_acc1']));
      }
    }

    return [trainLossList, testAcc1List];
  } catch (error) {
    throw new Error(`Error reading log file: ${error.message}`);
  }
}
import fs from 'fs';
import { parse } from 'json5';
describe('TestReadLog', () => {
    beforeEach(() => {
        jest.resetModules();
    });

    it('test_read_correct_data', () => {
        const mockFileContent = '{"test_acc1": 88.5, "train_loss": 0.75}\n{"test_acc1": 89.0, "train_loss": 0.70}';
        jest.spyOn(fs, 'readFileSync').mockImplementation(() => mockFileContent);

        const [trainLoss, testAcc1] = readLog('dummy_path.json');
        expect(trainLoss).toEqual([0.75, 0.70]);
        expect(testAcc1).toEqual([88.5, 89.0]);
    });

    it('test_read_correct_data_single', () => {
        const mockFileContent = '{"test_acc1": 88.5, "train_loss": 0.75}';
        jest.spyOn(fs, 'readFileSync').mockImplementation(() => mockFileContent);

        const [trainLoss, testAcc1] = readLog('dummy_path.json');
        expect(trainLoss).toEqual([0.75]);
        expect(testAcc1).toEqual([88.5]);
    });

    it('test_empty_file', () => {
        const mockFileContent = '';
        jest.spyOn(fs, 'readFileSync').mockImplementation(() => mockFileContent);

        const [trainLoss, testAcc1] = readLog('empty_file.json');
        expect(trainLoss).toEqual([]);
        expect(testAcc1).toEqual([]);
    });

    it('test_partial_data_entries', () => {
        const mockFileContent = '{"test_acc1": 88.5, "train_loss": 0.75}\n{"test_acc1": 90.0,"train_loss": 0.75,"f1":0.91}';
        jest.spyOn(fs, 'readFileSync').mockImplementation(() => mockFileContent);

        const [trainLoss, testAcc1] = readLog('partial_data_file.json');
        expect(trainLoss).toEqual([0.75, 0.75]);
        expect(testAcc1).toEqual([88.5, 90.0]);
    });
});
