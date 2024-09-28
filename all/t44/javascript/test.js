// Assume stringSideBySide function is defined here

describe('stringSideBySide', () => {

  test('equal length strings', () => {
    const str1 = "Hello\nWorld";
    const str2 = "Python\nCode";
    const result = stringSideBySide(str1, str2);
    const expected = "Hello                | Python              \nWorld                | Code                ";
    expect(result).toBe(expected);
  });

  test('first string longer', () => {
    const str1 = "Hello\nWorld\nTest";
    const str2 = "Python\nCode";
    const result = stringSideBySide(str1, str2);
    const expected = "Hello                | Python              \nWorld                | Code                \nTest                 |                     ";
    expect(result).toBe(expected);
  });

  test('second string longer', () => {
    const str1 = "Hello\nWorld";
    const str2 = "Python\nCode\nTest";
    const result = stringSideBySide(str1, str2);
    const expected = "Hello                | Python              \nWorld                | Code                \n                     | Test                ";
    expect(result).toBe(expected);
  });

  test('empty first string', () => {
    const str1 = "";
    const str2 = "Python\nCode";
    const result = stringSideBySide(str1, str2);
    const expected = "                     | Python              \n                     | Code                ";
    expect(result).toBe(expected);
  });

  test('custom column width', () => {
    const str1 = "Hello\nWorld";
    const str2 = "Python\nCode";
    const result = stringSideBySide(str1, str2, 10);
    const expected = "Hello      | Python    \nWorld      | Code      ";
    expect(result).toBe(expected);
  });

});