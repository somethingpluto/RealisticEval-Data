/**
 * Logs an item by printing it. Handles strings, numbers, arrays, and objects by printing
 * them directly or as a JSON-formatted string. Other types are reported as errors.
 * 
 * @param {any} item - The item to be logged. Can be of any type.
 * @returns {any} - The item to be logged. Can be of any type.
 */
function log(item) {
    try {
        if (typeof item === 'string' || typeof item === 'number' || typeof item === 'boolean') {
            console.log(item);
        } else if (Array.isArray(item)) {
            console.log(item);
        } else if (typeof item === 'object' && item !== null) {
            console.log(JSON.stringify(item, null, 2));
        } else {
            throw new Error('Unsupported type');
        }
    } catch (error) {
        console.error('Error logging item:', error.message);
    }
    return item;
}
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
