describe('TestLogFunction', () => {
    it('test_log_string', () => {
        const mockPrint = jest.spyOn(console, 'log').mockImplementation(() => {});

        log("Hello, world!");

        expect(mockPrint).toHaveBeenCalledWith("Hello, world!");
        mockPrint.mockRestore();
    });

    it('test_log_number', () => {
        const mockPrint = jest.spyOn(console, 'log').mockImplementation(() => {});

        log(123.456);

        expect(mockPrint).toHaveBeenCalledWith(123.456);
        mockPrint.mockRestore();
    });

    it('test_log_dictionary', () => {
        const mockPrint = jest.spyOn(console, 'log').mockImplementation(() => {});

        log({ key: "value", number: 42 });

        const expectedJsonOutput = JSON.stringify({ key: "value", number: 42 }, null, 4);
        expect(mockPrint).toHaveBeenCalledWith(expectedJsonOutput);
        mockPrint.mockRestore();
    });

    it('test_log_list', () => {
        const mockPrint = jest.spyOn(console, 'log').mockImplementation(() => {});

        log([1, 2, 3, 4, 5]);

        const expectedJsonOutput = JSON.stringify([1, 2, 3, 4, 5], null, 4);
        expect(mockPrint).toHaveBeenCalledWith(expectedJsonOutput);
        mockPrint.mockRestore();
    });
});