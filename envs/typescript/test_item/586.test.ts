// ... (previous code for context)
import { isUpperCase } from './utils'; // Assume this utility function exists

function isSnakeCase(input: string): boolean {
  if (input.length === 0) return false;
  if (isUpperCase(input[0])) return false;
  if (input.includes('_') && input.split('_').some(part => part.length === 0)) return false;
  return input.split('_').every(part => part.length > 0 && !isUpperCase(part[0]));
}
// ... (continuation of the code)
describe('isSnakeCase', () => {
    test('should return true for a valid snake_case string', () => {
        expect(isSnakeCase('snake_case')).toBe(true);
    });

    test('should return true for a valid snake_case string with multiple words', () => {
        expect(isSnakeCase('snake_case_example')).toBe(true);
    });

    test('should return false for a string that starts with an uppercase letter', () => {
        expect(isSnakeCase('Snake_Case')).toBe(false);
    });

    test('should return false for a string with mixed case letters', () => {
        expect(isSnakeCase('snakeCASE')).toBe(false);
    });

    test('should return false for a string with numbers', () => {
        expect(isSnakeCase('snake_case_123')).toBe(false);
    });

    test('should return false for an empty string', () => {
        expect(isSnakeCase('')).toBe(false);
    });
});
