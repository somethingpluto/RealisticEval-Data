describe('log function', () => {
    it('logs a string', () => {
        const mockConsoleLog = jest.spyOn(console, 'log');
        log('Hello, world!');
        expect(mockConsoleLog).toHaveBeenCalledWith('Hello, world!');
        mockConsoleLog.mockRestore();
    });

    it('logs a number', () => {
        const mockConsoleLog = jest.spyOn(console, 'log');
        log(42);
        expect(mockConsoleLog).toHaveBeenCalledWith(42);
        mockConsoleLog.mockRestore();
    });

    it('logs a list', () => {
        const mockConsoleLog = jest.spyOn(console, 'log');
        log([1, 2, 3]);
        expect(mockConsoleLog).toHaveBeenCalledWith([1, 2, 3]);
        mockConsoleLog.mockRestore();
    });

    it('logs a dictionary', () => {
        const mockConsoleLog = jest.spyOn(console, 'log');
        log({ key: 'value' });
        expect(mockConsoleLog).toHaveBeenCalledWith('{"key":"value"}');
        mockConsoleLog.mockRestore();
    });

    it('throws an error for unsupported type', () => {
        expect(() => log(undefined)).toThrowError('Unsupported type: undefined');
    });
});