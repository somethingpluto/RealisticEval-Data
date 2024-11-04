describe('TestCodeBlockRemover', () => {
  it('should handle a single code block', () => {
      const markdown = `
      This is a markdown with a code block.

      \`\`\`python
      print("Hello, World!")
      \`\`\`

      End of markdown.
      `;
      const expected = ['print("Hello, World!")'];
      const result = codeBlockRemover(markdown);
      expect(result).toEqual(expected);
  });

  it('should handle multiple code blocks', () => {
      const markdown = `
      First code block:

      \`\`\`python
      print("Hello, World!")
      \`\`\`

      Second code block:

      \`\`\`javascript
      console.log("Hello, World!");
      \`\`\`
      `;
      const expected = [
          'print("Hello, World!")',
          'console.log("Hello, World!");'
      ];
      const result = codeBlockRemover(markdown);
      expect(result).toEqual(expected);
  });

  it('should handle no code blocks', () => {
      const markdown = `
      This markdown has no code blocks.

      Just some plain text.
      `;
      const expected = [];
      const result = codeBlockRemover(markdown);
      expect(result).toEqual(expected);
  });

  it('should handle an empty code block', () => {
      const markdown = `
      Here is an empty code block:

      \`\`\`python
      \`\`\`

      End of markdown.
      `;
      const expected = [''];
      const result = codeBlockRemover(markdown);
      expect(result).toEqual(expected);
  });

  it('should handle a malformed code block', () => {
      const markdown = `
      This code block is missing ending:

      \`\`\`python
      print("Hello, World!")

      And some more text.
      `;
      const expected = [];
      const result = codeBlockRemover(markdown);
      expect(result).toEqual(expected);
  });
});