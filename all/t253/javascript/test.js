describe('log function', () => {
  test('logs a string', () => {
    const spy = jest.spyOn(console, 'log');
    log('Hello, world!');
    expect(spy).toHaveBeenCalledWith('Hello, world!');
    spy.mockRestore();
  });

  test('logs a number', () => {
    const spy = jest.spyOn(console, 'log');
    log(42);
    expect(spy).toHaveBeenCalledWith(42);
    spy.mockRestore();
  });

  test('logs a list (array)', () => {
    const spy = jest.spyOn(console, 'log');
    log([1, 2, 3]);
    expect(spy).toHaveBeenCalledWith([1, 2, 3]);
    spy.mockRestore();
  });

  test('logs a dictionary (object)', () => {
    const spy = jest.spyOn(console, 'log');
    log({ key: 'value' });
    expect(spy).toHaveBeenCalledWith({ key: 'value' });
    spy.mockRestore();
  });

  test('logs other types as errors', () => {
    const spy = jest.spyOn(console, 'error');
    log(new Date());
    expect(spy).toHaveBeenCalled();
    spy.mockRestore();
  });
});