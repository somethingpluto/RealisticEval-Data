const fs = require('fs');
describe('readLog', () => {
    
    test('reads correctly formatted JSON lines', () => {
        // Mock file content
        const mockFileContent = '{"test_acc1": 88.5, "train_loss": 0.75}\n' +
                                '{"test_acc1": 89.0, "train_loss": 0.70}';
        
        // Mock the fs.readFileSync method
        jest.spyOn(fs, 'readFileSync').mockReturnValue(mockFileContent);

        // Call the function and assert results
        const { trainLossList, testAcc1List } = readLog("dummy_path.json");
        expect(trainLossList).toEqual([0.75, 0.70]);
        expect(testAcc1List).toEqual([88.5, 89.0]);
        
        // Restore the original implementation
        fs.readFileSync.mockRestore();
    });

    test('reads correctly formatted JSON lines - single entry', () => {
        const mockFileContent = '{"test_acc1": 88.5, "train_loss": 0.75}';
        
        jest.spyOn(fs, 'readFileSync').mockReturnValue(mockFileContent);
        
        const { trainLossList, testAcc1List } = readLog("dummy_path.json");
        expect(trainLossList).toEqual([0.75]);
        expect(testAcc1List).toEqual([88.5]);
        
        fs.readFileSync.mockRestore();
    });

    test('reads an empty file', () => {
        jest.spyOn(fs, 'readFileSync').mockReturnValue("");

        const { trainLossList, testAcc1List } = readLog("empty_file.json");
        expect(trainLossList).toEqual([]);
        expect(testAcc1List).toEqual([]);

        fs.readFileSync.mockRestore();
    });

    test('handles partial data entries', () => {
        const mockFileContent = '{"test_acc1": 88.5, "train_loss": 0.75}\n' +
                                '{"test_acc1": 90.0, "train_loss": 0.75, "f1": 0.91}'; // Missing train_loss
        
        jest.spyOn(fs, 'readFileSync').mockReturnValue(mockFileContent);

        const { trainLossList, testAcc1List } = readLog("partial_data_file.json");
        expect(trainLossList).toEqual([0.75, 0.75]); // Only one complete entry
        expect(testAcc1List).toEqual([88.5, 90.0]);
        
        fs.readFileSync.mockRestore();
    });
});
