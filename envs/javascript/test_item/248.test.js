/**
 * Recursively sanitizes a dictionary by removing specific keys.
 *
 * @param {Object} data - The original dictionary to sanitize.
 * @param {Array<string>=} keyToRemove - An optional list of keys to remove.
 * @returns {Object} The sanitized dictionary.
 */
function sanitizeData(data, keyToRemove = null) {
    // If keyToRemove is not provided, return the data as is
    if (!keyToRemove || !Array.isArray(keyToRemove) || keyToRemove.length === 0) {
        return data;
    }

    // Helper function to recursively sanitize the data
    function recursiveSanitize(obj) {
        // If the current data is not an object, return it as is
        if (typeof obj !== 'object' || obj === null || Array.isArray(obj)) {
            return obj;
        }

        // Create a new object to store the sanitized data
        const sanitizedObj = {};

        // Iterate over the keys of the current object
        for (const key in obj) {
            if (obj.hasOwnProperty(key)) {
                // If the key is not in the list of keys to remove, process it
                if (!keyToRemove.includes(key)) {
                    // Recursively sanitize the value
                    sanitizedObj[key] = recursiveSanitize(obj[key]);
                }
            }
        }

        return sanitizedObj;
    }

    // Start the recursive sanitization process
    return recursiveSanitize(data);
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
