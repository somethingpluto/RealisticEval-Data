describe('Colors', () => {
    describe('red', () => {
      it('should return text wrapped in red color code', () => {
        const result = Colors.red('Hello');
        expect(result).toBe('\x1b[31mHello\x1b[0m'); // Assuming ANSI escape codes for colors
      });
    });
  
    describe('green', () => {
      it('should return text wrapped in green color code', () => {
        const result = Colors.green('Hello');
        expect(result).toBe('\x1b[32mHello\x1b[0m'); // Assuming ANSI escape codes for colors
      });
    });
  
    describe('blue', () => {
      it('should return text wrapped in blue color code', () => {
        const result = Colors.blue('Hello');
        expect(result).toBe('\x1b[34mHello\x1b[0m'); // Assuming ANSI escape codes for colors
      });
    });
  
    describe('yellow', () => {
      it('should return text wrapped in yellow color code', () => {
        const result = Colors.yellow('Hello');
        expect(result).toBe('\x1b[33mHello\x1b[0m'); // Assuming ANSI escape codes for colors
      });
    });
  
    describe('magenta', () => {
      it('should return text wrapped in magenta color code', () => {
        const result = Colors.magenta('Hello');
        expect(result).toBe('\x1b[35mHello\x1b[0m'); // Assuming ANSI escape codes for colors
      });
    });
  
    describe('cyan', () => {
      it('should return text wrapped in cyan color code', () => {
        const result = Colors.cyan('Hello');
        expect(result).toBe('\x1b[36mHello\x1b[0m'); // Assuming ANSI escape codes for colors
      });
    });
  });
  