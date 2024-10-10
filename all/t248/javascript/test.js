describe('sanitizeData', () => {
  it('removes specified keys from the input dictionary', () => {
    const data = {
      name: 'John Doe',
      email: 'john.doe@example.com',
      password: '123456'
    };
    const keyToRemove = ['email', 'password'];

    const result = sanitizeData(data, keyToRemove);

    expect(result).toEqual({
      name: 'John Doe'
    });
  });

  it('does not modify the input dictionary if no keys are specified', () => {
    const data = {
      name: 'John Doe',
      email: 'john.doe@example.com',
      password: '123456'
    };

    const result = sanitizeData(data);

    expect(result).toEqual({
      name: 'John Doe',
      email: 'john.doe@example.com',
      password: '123456'
    });
  });

  it('returns an empty object if both input and keyToRemove are empty', () => {
    const data = {};
    const keyToRemove = [];

    const result = sanitizeData(data, keyToRemove);

    expect(result).toEqual({});
  });

  it('handles nested dictionaries correctly', () => {
    const data = {
      user: {
        name: 'John Doe',
        email: 'john.doe@example.com',
        address: {
          city: 'New York',
          zip: '10001'
        }
      },
      password: '123456'
    };
    const keyToRemove = ['user.email', 'password'];

    const result = sanitizeData(data, keyToRemove);

    expect(result).toEqual({
      user: {
        name: 'John Doe',
        address: {
          city: 'New York',
          zip: '10001'
        }
      }
    });
  });
});