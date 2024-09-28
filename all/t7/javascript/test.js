const Logger = require('./logger');  // Import your Logger class
jest.mock('console');

describe('Logger', () => {
    let logger;
    const loggerName = 'test_logger';

    beforeEach(() => {
        logger = new Logger(loggerName);
        jest.spyOn(global.console, 'debug').mockImplementation(() => {});
        jest.spyOn(global.console, 'info').mockImplementation(() => {});
        jest.spyOn(global.console, 'warn').mockImplementation(() => {});
        jest.spyOn(global.console, 'error').mockImplementation(() => {});
    });

    afterEach(() => {
        jest.clearAllMocks();
    });

    test('should log debug messages to console.debug', () => {
        const message = "This is a debug message";
        logger.log('DEBUG', message);
        expect(console.debug).toHaveBeenCalledWith(expect.stringContaining(message));
    });

    test('should log info messages to console.info', () => {
        const message = "This is an info message";
        logger.log('INFO', message);
        expect(console.info).toHaveBeenCalledWith(expect.stringContaining(message));
    });

    test('should log warning messages to console.warn', () => {
        const message = "This is a warning message";
        logger.log('WARNING', message);
        expect(console.warn).toHaveBeenCalledWith(expect.stringContaining(message));
    });

    test('should log error messages to console.error', () => {
        const message = "This is an error message";
        logger.log('ERROR', message);
        expect(console.error).toHaveBeenCalledWith(expect.stringContaining(message));
    });

    test('should log critical messages to console.error', () => {
        const message = "This is a critical message";
        logger.log('CRITICAL', message);
        expect(console.error).toHaveBeenCalledWith(expect.stringContaining(message));
    });
});