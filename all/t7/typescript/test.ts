import { Logger, LogLevel } from './logger';
import { jest } from '@jest/globals';

describe('Logger', () => {
    let logger: Logger;
    const loggerName = 'test_logger';

    beforeEach(() => {
        logger = new Logger(loggerName);
    });

    test('debug logging', () => {
        const message = "This is a debug message";
        console.debug = jest.fn();
        
        logger.debug(message);

        expect(console.debug).toHaveBeenCalledWith(expect.stringContaining(message));
    });

    test('info logging', () => {
        const message = "This is an info message";
        console.info = jest.fn();

        logger.info(message);

        expect(console.info).toHaveBeenCalledWith(expect.stringContaining(message));
    });

    test('warning logging', () => {
        const message = "This is a warning message";
        console.warn = jest.fn();

        logger.warning(message);

        expect(console.warn).toHaveBeenCalledWith(expect.stringContaining(message));
    });

    test('error logging', () => {
        const message = "This is an error message";
        console.error = jest.fn();

        logger.error(message);

        expect(console.error).toHaveBeenCalledWith(expect.stringContaining(message));
    });

    test('critical logging', () => {
        const message = "This is a critical message";
        console.error = jest.fn();

        logger.critical(message);

        expect(console.error).toHaveBeenCalledWith(expect.stringContaining('CRITICAL:'));
        expect(console.error).toHaveBeenCalledWith(expect.stringContaining(message));
    });
});