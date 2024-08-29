// Import the deepEqual function if it's in a different file
// const { deepEqual } = require('./path/to/your/deepEqual');

describe('deepEqual', () => {
  test('should return true for identical primitive values and false for different values', () => {
    expect(deepEqual(5, 5)).toBe(true);
    expect(deepEqual('hello', 'hello')).toBe(true);
    expect(deepEqual(5, 7)).toBe(false);
    expect(deepEqual('hello', 'world')).toBe(false);
  });

  test('should return true for identical nested objects and false for different ones', () => {
    const obj1 = { a: 1, b: { c: 2 } };
    const obj2 = { a: 1, b: { c: 2 } };
    const obj3 = { a: 1, b: { c: 3 } };
    expect(deepEqual(obj1, obj2)).toBe(true);
    expect(deepEqual(obj1, obj3)).toBe(false);
  });

  test('should handle arrays correctly, returning true for identical arrays and false for different ones', () => {
    const array1 = [1, 2, 3];
    const array2 = [1, 2, 3];
    const array3 = [1, 2, 4];
    expect(deepEqual(array1, array2)).toBe(true);
    expect(deepEqual(array1, array3)).toBe(false);
  });

  test('should return false when comparing objects to primitives, arrays to objects, etc.', () => {
    const obj = { a: 1 };
    const arr = [1, 2, 3];
    expect(deepEqual(obj, arr)).toBe(false);
    expect(deepEqual(arr, obj)).toBe(false);
    expect(deepEqual(42, obj)).toBe(false);
    expect(deepEqual('text', arr)).toBe(false);
  });

  test('should correctly compare complex nested structures', () => {
    const complex1 = { a: { b: [1, 2, { c: 3 }] }, d: 'text' };
    const complex2 = { a: { b: [1, 2, { c: 3 }] }, d: 'text' };
    const complex3 = { a: { b: [1, 2, { c: 4 }] }, d: 'text' };
    expect(deepEqual(complex1, complex2)).toBe(true);
    expect(deepEqual(complex1, complex3)).toBe(false);
  });
});