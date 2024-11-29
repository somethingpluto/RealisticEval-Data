function sanitizeData(data, keyToRemove = null) {
    // Recursively sanitize an object by removing specific keys.
    if (keyToRemove === null) {
        keyToRemove = new Set([
            "email", "pc_conflicts", "metadata", 
            "eligible_student_paper_prize", "talk_poster", 
            "submitted_at", "decision", "status", 
            "submitted", "submission"
        ]);
    }

    if (typeof data === 'object' && !Array.isArray(data) && data !== null) {
        const result = {};
        for (const [key, value] of Object.entries(data)) {
            if (!keyToRemove.has(key)) {
                result[key] = sanitizeData(value, keyToRemove);
            }
        }
        return result;
    } else if (Array.isArray(data)) {
        return data.map(value => sanitizeData(value, keyToRemove));
    } else {
        return data;
    }
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
