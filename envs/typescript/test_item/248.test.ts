import { Dictionary } from "lodash";

/**
 * Recursively sanitizes a dictionary by removing specific keys.
 * 
 * @param data - The original dictionary to sanitize.
 * @param keyToRemove - An optional list of keys to remove. If not provided, defaults to a predefined set of keys.
 * @returns The sanitized dictionary.
 */
function sanitizeData(data: Dictionary<any>, keyToRemove?: string[]): Dictionary<any> {
    // Your implementation goes here
}
import { Dictionary } from "lodash";
describe('TestSanitizeData', () => {
  describe('test_empty_dict', () => {
    it('should return an empty dictionary when given an empty dictionary', () => {
      const data = {};
      const keyToRemove = ["email", "metadata"];
      const expected = {};

      expect(sanitizeData(data, keyToRemove)).toEqual(expected);
    });
  });

  describe('test_remove_default_keys', () => {
    it('should remove default keys from a nested structure', () => {
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
  });

  describe('test_specified_key_to_remove', () => {
    it('should remove a specified key from the dictionary', () => {
      const data = {
        name: "John Doe",
        location: "Earth",
        email: "johndoe@example.com"
      };
      const expected = {
        name: "John Doe",
        location: "Earth"
      };

      expect(sanitizeData(data, ["email"])).toEqual(expected);
    });
  });
});
