describe('TestLogFunction', () => {
  beforeEach(() => {
      jest.spyOn(console, 'log').mockImplementation(jest.fn());
  });

  afterEach(() => {
      console.log.mockRestore();
  });

  test('test_log_string', () => {
      /** Test logging a simple string */
      log("Hello, world!");
      expect(console.log).toHaveBeenCalledWith("Hello, world!");
  });

  test('test_log_number', () => {
      /** Test logging a number */
      log(123.456);
      expect(console.log).toHaveBeenCalledWith(123.456);
  });

  test('test_log_dictionary', () => {
      /** Test logging a dictionary as JSON */
      log({ key: "value", number: 42 });
      const expectedJsonOutput = JSON.stringify({ key: "value", number: 42 }, null, 4);
      expect(console.log).toHaveBeenCalledWith(expectedJsonOutput);
  });

  test('test_log_list', () => {
      /** Test logging a list as JSON */
      log([1, 2, 3, 4, 5]);
      const expectedJsonOutput = JSON.stringify([1, 2, 3, 4, 5], null, 4);
      expect(console.log).toHaveBeenCalledWith(expectedJsonOutput);
  });
});