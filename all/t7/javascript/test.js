describe('Logger', () => {
    let logger;

    beforeEach(() => {
        logger = new Logger('test-logger');
    });

    it('should log an info message', async () => {
        const spy = jest.spyOn(console, 'log');
        logger.log('info', 'This is an info message');
        expect(spy).toHaveBeenCalledWith(expect.any(Object));
        spy.mockRestore();
    });

    it('should log a debug message', async () => {
        const spy = jest.spyOn(console, 'log');
        logger.log('debug', 'This is a debug message');
        expect(spy).toHaveBeenCalledWith(expect.any(Object));
        spy.mockRestore();
    });
});