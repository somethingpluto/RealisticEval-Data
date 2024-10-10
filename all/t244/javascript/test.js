describe('methodArgTypeCheck', () => {
  it('should throw an error if the arguments do not match the expected types', () => {
    const mockMethod = jest.fn();

    const mockClass = class {
      constructor() {
        this.method = mockMethod;
      }
    };

    const instance = new mockClass();
    const mockFunction = instance.method;

    expect(() => {
      methodArgTypeCheck(mockFunction, 'invalidArgument');
    }).toThrowError('Invalid argument type');
  });

  it('should not throw an error if the arguments match the expected types', () => {
    const mockMethod = jest.fn((arg1, arg2) => {});

    const mockClass = class {
      constructor() {
        this.method = mockMethod;
      }
    };

    const instance = new mockClass();
    const mockFunction = instance.method;

    expect(() => {
      methodArgTypeCheck(mockFunction, 'validArgument1', 'validArgument2');
    }).not.toThrowError();
  });

  it('should ignore excluded parameters', () => {
    const mockMethod = jest.fn((arg1, arg2) => {});

    const mockClass = class {
      constructor() {
        this.method = mockMethod;
      }
    };

    const instance = new mockClass();
    const mockFunction = instance.method;

    expect(() => {
      methodArgTypeCheck(mockFunction, 'validArgument1', 'validArgument2', { exclude: ['arg1'] });
    }).not.toThrowError();
  });
});