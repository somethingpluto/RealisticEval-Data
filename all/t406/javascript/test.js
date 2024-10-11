describe('Colors', () => {
    it('should return red colored text', () => {
      const result = Colors.red('Hello');
      expect(result).toBe('\x1b[31mHello\x1b[0m');
    });
  
    it('should return green colored text', () => {
      const result = Colors.green('Hello');
      expect(result).toBe('\x1b[32mHello\x1b[0m');
    });
  
    it('should return blue colored text', () => {
      const result = Colors.blue('Hello');
      expect(result).toBe('\x1b[34mHello\x1b[0m');
    });
  
    it('should return yellow colored text', () => {
      const result = Colors.yellow('Hello');
      expect(result).toBe('\x1b[33mHello\x1b[0m');
    });
  
    it('should return magenta colored text', () => {
      const result = Colors.magenta('Hello');
      expect(result).toBe('\x1b[35mHello\x1b[0m');
    });
  
    it('should return cyan colored text', () => {
      const result = Colors.cyan('Hello');
      expect(result).toBe('\x1b[36mHello\x1b[0m');
    });
  });