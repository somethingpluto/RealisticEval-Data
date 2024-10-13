describe('Logger', () => {
    let loggerName: string;
    let logger: Logger;
  
    beforeEach(() => {
      loggerName = 'TestLogger';
      logger = new Logger(loggerName);
    });
  
    describe('initialization', () => {
      it('should initialize the logger with the correct name and level', () => {
        expect(logger.logger.name).toBe(loggerName);
        expect(logger.logger.level).toBe('debug');
      });
    });
  
    describe('default logging level', () => {
      it('should default to DEBUG level if not specified', () => {
        const loggerDefault = new Logger('DefaultLogger');
        expect(loggerDefault.logger.level).toBe('debug');
      });
    });
  
    describe('console handler added', () => {
      it('should add a console handler to the logger', () => {
        const handlers = logger.logger.appender.getAppenders();
        expect(handlers.length).toBeGreaterThan(0);
        expect(handlers[0].type).toBe('console');
      });
    });
  });