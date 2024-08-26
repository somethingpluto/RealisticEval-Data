describe('parseMarkdownTitles', () => {
  test('should correctly parse a single heading', () => {
    const markdown = '# Heading 1';
    const expected = [{ title: 'Heading 1', sub: [] }];
    expect(parseMarkdownTitles(markdown)).toEqual(expected);
  });

  test('should correctly parse multiple headings at the same level', () => {
    const markdown = '# Heading 1\n# Heading 2';
    const expected = [
      { title: 'Heading 1', sub: [] },
      { title: 'Heading 2', sub: [] }
    ];
    expect(parseMarkdownTitles(markdown)).toEqual(expected);
  });

  test('should correctly parse nested headings', () => {
    const markdown = '# Heading 1\n## Subheading 1.1\n## Subheading 1.2';
    const expected = [
      { title: 'Heading 1', sub: [
        { title: 'Subheading 1.1', sub: [] },
        { title: 'Subheading 1.2', sub: [] }
      ]}
    ];
    expect(parseMarkdownTitles(markdown)).toEqual(expected);
  });

test('should handle headings with inconsistent nesting', () => {
  const markdown = '# Heading 1\n## Subheading 1.1\n### Subheading 1.1.1';
  const expected = [
    { title: 'Heading 1', sub: [
      { title: 'Subheading 1.1', sub: [
        { title: 'Subheading 1.1.1', sub: [] }
      ]}
    ]}
  ];
  expect(parseMarkdownTitles(markdown)).toEqual(expected);
});

  test('should correctly parse a complex nested structure with mixed headings', () => {
    const markdown = '# Heading 1\n## Subheading 1.1\n### Sub-subheading 1.1.1\n#### Sub-sub-subheading 1.1.1.1\n## Subheading 1.2';
    const expected = [
      { title: 'Heading 1', sub: [
        { title: 'Subheading 1.1', sub: [
          { title: 'Sub-subheading 1.1.1', sub: [
            { title: 'Sub-sub-subheading 1.1.1.1', sub: [] }
          ]}
        ]},
        { title: 'Subheading 1.2', sub: [] }
      ]}
    ];
    expect(parseMarkdownTitles(markdown)).toEqual(expected);
  });
});
