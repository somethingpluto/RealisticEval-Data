import * as log4js from 'log4js';

class Logger {
  private logger: log4js.Logger;

  constructor(name: string, level: log4js.Level = 'debug') {
    // Configure log4js
    log4js.configure({
      appenders: {
        console: { type: 'console' }
      },
      categories: {
        default: { appenders: ['console'], level }
      }
    });

    // Create logger
    this.logger = log4js.getLogger(name);
  }

  public log(level: log4js.Level, message: string): void {
    switch (level) {
      case 'debug':
        this.logger.debug(message);
        break;
      case 'info':
        this.logger.info(message);
        break;
      case 'warn':
        this.logger.warn(message);
        break;
      case 'error':
        this.logger.error(message);
        break;
      case 'fatal':
        this.logger.fatal(message);
        break;
      default:
        throw new Error('Invalid log level');
    }
  }
}