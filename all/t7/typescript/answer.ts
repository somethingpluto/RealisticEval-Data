type LogLevel = 'debug' | 'info' | 'warning' | 'error' | 'critical';

class Logger {
    private name: string;
    private level: LogLevel;
    private levelPriority: Record<LogLevel, number> = {
        'debug': 10,
        'info': 20,
        'warning': 30,
        'error': 40,
        'critical': 50
    };

    constructor(name: string, level: LogLevel = 'debug') {
        this.name = name;
        this.level = level;
    }

    private log(level: LogLevel, message: string) {
        // If the current message level is less than the logger level, do not log
        if (this.levelPriority[level] < this.levelPriority[this.level]) {
            return;
        }

        const timestamp = new Date().toISOString();
        const formattedMessage = `${timestamp} - ${level.toUpperCase()} - ${this.name}: ${message}`;

        switch (level) {
            case 'debug':
                console.debug(formattedMessage);
                break;
            case 'info':
                console.info(formattedMessage);
                break;
            case 'warning':
                console.warn(formattedMessage);
                break;
            case 'error':
                console.error(formattedMessage);
                break;
            case 'critical':
                console.error(`CRITICAL: ${formattedMessage}`);
                break;
        }
    }

    public debug(message: string) {
        this.log('debug', message);
    }

    public info(message: string) {
        this.log('info', message);
    }

    public warning(message: string) {
        this.log('warning', message);
    }

    public error(message: string) {
        this.log('error', message);
    }

    public critical(message: string) {
        this.log('critical', message);
    }
}

// Example usage:
const logger = new Logger('myModuleName');
logger.debug('This is a debug message.');
logger.info('This is an info message.');
logger.warning('This is a warning message.');
logger.error('This is an error message.');
logger.critical('This is a critical message.');