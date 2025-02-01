/**
 * Safely formats a template string by replacing placeholders with corresponding values
 * from the provided keyword arguments. If a placeholder does not have a corresponding
 * value in kwargs, it remains unchanged.
 *
 * @param {string} template - The string template containing placeholders in the form {key}.
 * @param {Object} [kwargs] - Keyword arguments that map keys to their replacement values.
 * @returns {string} The formatted string with placeholders replaced by values.
 */
function safeFormat(template, kwargs = {}) {
    return template.replace(/{(\w+)}/g, (match, key) => kwargs[key] || match);
}
describe('TestSafeFormat', () => {
  describe('test_full_replacement', () => {
      it('should fully replace all placeholders with corresponding values', () => {
          const template = "Hello, {name}! Welcome to {place}.";
          const result = safeFormat(template, { name: "Alice", place: "Wonderland" });
          const expected = "Hello, Alice! Welcome to Wonderland.";
          expect(result).toEqual(expected);
      });
  });

  describe('test_partial_replacement', () => {
      it('should partially replace placeholders with corresponding values', () => {
          const template = "Hello, {name}! Welcome to {place}.";
          const result = safeFormat(template, { name: "Alice" });
          const expected = "Hello, Alice! Welcome to {place}.";
          expect(result).toEqual(expected);
      });
  });

  describe('test_no_replacement', () => {
      it('should not replace any placeholders when none are provided', () => {
          const template = "Hello, world!";
          const result = safeFormat(template);
          const expected = "Hello, world!";
          expect(result).toEqual(expected);
      });
  });

  describe('test_missing_placeholder', () => {
      it('should leave placeholders unchanged when a value is missing', () => {
          const template = "My name is {name}, and I live in {city}.";
          const result = safeFormat(template, { name: "Alice" });
          const expected = "My name is Alice, and I live in {city}.";
          expect(result).toEqual(expected);
      });
  });

  describe('test_numeric_values', () => {
      it('should handle numeric values correctly', () => {
          const template = "Your score is {score} out of {total}.";
          const result = safeFormat(template, { score: 85, total: 100 });
          const expected = "Your score is 85 out of 100.";
          expect(result).toEqual(expected);
      });
  });
});
