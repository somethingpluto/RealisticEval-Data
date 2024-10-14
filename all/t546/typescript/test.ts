describe('TestReadTsvFromStdin', () => {
    it('test basic TSV input', async () => {
      const mockStdin = 'col1\tcol2\tcol3\nval1\tval2\tval3\n';
      process.stdin.setEncoding('utf8');
      process.stdin.unshift(mockStdin);
  
      const expectedOutput = [['col1', 'col2', 'col3'], ['val1', 'val2', 'val3']];
      const result = await readTsvFromStdin();
  
      expect(result).toEqual(expectedOutput);
    });
  
    it('test single column', async () => {
      const mockStdin = 'col1\nval1\nval2\n';
      process.stdin.setEncoding('utf8');
      process.stdin.unshift(mockStdin);
  
      const expectedOutput = [['col1'], ['val1'], ['val2']];
      const result = await readTsvFromStdin();
  
      expect(result).toEqual(expectedOutput);
    });
  });