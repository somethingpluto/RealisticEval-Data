describe('prependToEachLine', () => {
  it('should prepend prefix to each line of the file', async () => {
    const tempFilePath = path.join(__dirname, 'temp.txt');
    const content = "line1\nline2\nline3";

    // Create a temporary file with initial content
    fs.writeFileSync(tempFilePath, content);

    // Call the function
    prependToEachLine(tempFilePath, 'prefix_');

    // Read the updated file and check if the content is correct
    let updatedContent = fs.readFileSync(tempFilePath, 'utf8');
    expect(updatedContent).toBe("prefix_line1\nprefix_line2\nprefix_line3");

    // Clean up - remove the temporary file
    fs.unlinkSync(tempFilePath);
  });
});