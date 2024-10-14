const safeFormat = require('./path-to-your-safe-format-function'); // Adjust the path accordingly

describe('safeFormat', () => {
  test('replaces placeholders with corresponding values', () => {
    const template = 'Hello, {name}!';
    const result = safeFormat(template, { name: 'Alice' });
    expect(result).toBe('Hello, Alice!');
  });

  test('leaves unmatching placeholders unchanged', () => {
    const template = 'Hello, {name} and {age}';
    const result = safeFormat(template, { name: 'Alice' });
    expect(result).toBe('Hello, Alice and {age}');
  });

  test('handles empty template correctly', () => {
    const template = '';
    const result = safeFormat(template);
    expect(result).toBe('');
  });

  test('handles null or undefined inputs gracefully', () => {
    const template = null;
    const result = safeFormat(template);
    expect(result).toBe(null);

    const resultWithUndefined = safeFormat(undefined);
    expect(resultWithUndefined).toBe(undefined);
  });

  test('works with nested objects', () => {
    const template = 'Hello, {user.name}!';
    const result = safeFormat(template, { user: { name: 'Alice' } });
    expect(result).toBe('Hello, Alice!');
  });
});