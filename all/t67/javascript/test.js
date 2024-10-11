describe('parseXamlToDict', () => {
  it('should correctly parse XAML file and return a dictionary', async () => {
    const xamlFilePath = path.join(__dirname, 'test.xml'); // Replace with actual test XML file path
    const expectedOutput = { key1: 'value1', key2: 'value2' }; // Replace with expected output

    const result = await parseXamlToDict(xamlFilePath);
    expect(result).toEqual(expectedOutput);
  });

  it('should handle empty XAML file gracefully', async () => {
    const xamlFilePath = path.join(__dirname, 'empty_test.xml'); // Replace with actual empty test XML file path
    const expectedOutput = {};

    const result = await parseXamlToDict(xamlFilePath);
    expect(result).toEqual(expectedOutput);
  });
});