describe('Logger', () => {
    let loggerName;
    let logger;

    beforeEach(() => {
        loggerName = 'TestLogger';
        logger = new Logger(loggerName);
    });

    it('initializes with the correct name and level', () => {
        expect(logger.logger.name).toBe(loggerName);
        expect(logger.logger.level).toBe('debug');
    });

    it('defaults to DEBUG level if not specified', () => {
        const loggerDefault = new Logger('DefaultLogger');
        expect(loggerDefault.logger.level).toBe('debug');
    });

    it('adds a console handler to the logger', () => {
        const handlers = logger.logger.transports;
        expect(handlers.length).toBeGreaterThan(0);
        expect(handlers[0] instanceof winston.transports.Console).toBe(true);
    });
});