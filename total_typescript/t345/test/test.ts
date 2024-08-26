describe('toQueryString', () => {
  test('should convert simple object to query string', () => {
    const input = { name: 'John', age: 30 };
    const expected = 'name=John&age=30';
    expect(toQueryString(input)).toBe(expected);
  });

  test('should handle nested objects', () => {
    const input = { user: { name: 'Alice', age: 25 }, active: true };
    const expected = 'user[name]=Alice&user[age]=25&active=true';
    expect(toQueryString(input)).toBe(expected);
  });

  test('should handle arrays with primitive values', () => {
    const input = { ids: [1, 2, 3] };
    const expected = 'ids[]=1&ids[]=2&ids[]=3';
    expect(toQueryString(input)).toBe(expected);
  });

  test('should handle arrays containing objects', () => {
    const input = {
      users: [
        { name: 'Bob', age: 20 },
        { name: 'Tom', age: 22 }
      ]
    };
    const expected = 'users[0][name]=Bob&users[0][age]=20&users[1][name]=Tom&users[1][age]=22';
    expect(toQueryString(input)).toBe(expected);
  });

  test('should handle mixed nested structures (arrays and objects)', () => {
    const input = {
      group: {
        id: 10,
        members: [{ name: 'Sam' }, { name: 'Max' }]
      },
      active: true
    };
    const expected = 'group[id]=10&group[members][0][name]=Sam&group[members][1][name]=Max&active=true';
    expect(toQueryString(input)).toBe(expected);
  });
});