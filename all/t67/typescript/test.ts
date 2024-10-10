describe('parseXamlToDict', () => {
  it('should parse XAML and return correct dictionary', async () => {
    const xamlContent = `
      <root>
        <String key="key1">value1</String>
        <String key="key2">value2</String>
      </root>
    `;

    // Write the mock XAML content to a temporary file
    const tempFilePath = '/tmp/temp.xaml';
    fs.writeFileSync(tempFilePath, xamlContent);

    try {
      const result = await parseXamlToDict(tempFilePath);
      expect(result).toEqual({ key1: 'value1', key2: 'value2' });
    } finally {
      // Clean up the temporary file
      fs.unlinkSync(tempFilePath);
    }
  });

  it('should handle empty XAML', async () => {
    const xamlContent = '<root></root>';

    // Write the mock XAML content to a temporary file
    const tempFilePath = '/tmp/temp-empty.xaml';
    fs.writeFileSync(tempFilePath, xamlContent);

    try {
      const result = await parseXamlToDict(tempFilePath);
      expect(result).toEqual({});
    } finally {
      // Clean up the temporary file
      fs.unlinkSync(tempFilePath);
    }
  });

  it('should throw an error if file does not exist', async () => {
    const nonExistentFilePath = '/non-existent-file.xaml';

    await expect(parseXamlToDict(nonExistentFilePath)).rejects.toThrow();
  });
});
