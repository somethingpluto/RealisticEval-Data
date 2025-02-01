/**
 * Recursively sanitizes a dictionary by removing specific keys.
 *
 * @param {Object} data - The original dictionary to sanitize.
 * @param {Array<string>=} keyToRemove - An optional list of keys to remove.
 * @returns {Object} The sanitized dictionary.
 */
function sanitizeData(data, keyToRemove = null) {
    // If the data is not an object or is null, return it as is
    if (typeof data !== 'object' || data === null) {
        return data;
    }

    // If no keys to remove are specified, return the data as is
    if (!keyToRemove || !Array.isArray(keyToRemove)) {
        return data;
    }

    // Create a shallow copy of the data to avoid mutating the original object
    const sanitizedData = { ...data };

    // Iterate over each key in the list of keys to remove
    keyToRemove.forEach(key => {
        // If the key exists in the data, delete it
        if (sanitizedData.hasOwnProperty(key)) {
            delete sanitizedData[key];
        }
    });

    // Recursively sanitize each value in the data
    for (const key in sanitizedData) {
        if (sanitizedData.hasOwnProperty(key)) {
            sanitizedData[key] = sanitizeData(sanitizedData[key], keyToRemove);
        }
    }

    return sanitizedData;
}
describe('TestSanitizeData', () => {
  it('test_empty_dict', () => {
      // Test with an empty dictionary.
      const data = {};
      const keyToRemove = ["email", "metadata"];

      const expected = {};
      expect(sanitizeData(data, keyToRemove)).toEqual(expected);
  });

  it('test_remove_default_keys', () => {
      // Test removing default keys from a nested structure.
      const data = {
          name: "John Doe",
          email: "johndoe@example.com",
          metadata: { submitted_at: "2021-07-10", status: "pending" },
          comments: ["Good", "Needs review"]
      };
      const keyToRemove = ["email", "metadata"];
      const expected = {
          name: "John Doe",
          comments: ["Good", "Needs review"]
      };
      expect(sanitizeData(data, keyToRemove)).toEqual(expected);
  });

  it('test_specified_key_to_remove', () => {
      // Test removing a specified key from the dictionary.
      const data = {
          name: "John Doe",
          location: "Earth",
          email: "johndoe@example.com"
      };
      const expected = {
          name: "John Doe",
          location: "Earth"
      };
      expect(sanitizeData(data, keyToRemove: ["email"])).toEqual(expected);
  });
});
