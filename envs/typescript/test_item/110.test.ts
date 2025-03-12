import { v4 as uuidv4 } from 'uuid';

function generateUUID(): string {
  let uuid = uuidv4();
  let hasUppercase = false, hasLowercase = false, hasDigit = false;

  while (!hasUppercase || !hasLowercase || !hasDigit) {
    if (!hasUppercase) hasUppercase = /[A-Z]/.test(uuid);
    if (!hasLowercase) hasLowercase = /[a-z]/.test(uuid);
    if (!hasDigit) hasDigit = /\d/.test(uuid);

    if (!hasUppercase || !hasLowercase || !hasDigit) {
      uuid = uuidv4();
    }
  }

  return uuid;
}
describe('generateUUID', () => {

    test('should return a string', () => {
        const result: string = generateUUID();
        expect(typeof result).toBe('string');
    });

    test('should return a string of length 36', () => {
        const result: string = generateUUID();
        expect(result.length).toBe(36);
    });

    test('should generate different UUIDs on consecutive calls', () => {
        const uuid1: string = generateUUID();
        const uuid2: string = generateUUID();
        expect(uuid1).not.toBe(uuid2);
    });

    test('should generate UUIDs that include uppercase', () => {
        const result: string = generateUUID();
        expect(/[A-Z]/.test(result)).toBe(true); // At least one uppercase letter
    });

    test('should generate UUIDs that include lowercase letters', () => {
        const result: string = generateUUID();
        expect(/[a-z]/.test(result)).toBe(true); // At least one lowercase letter
    });

    test('should generate UUIDs that include digits', () => {
        const result: string = generateUUID();
        expect(/[0-9]/.test(result)).toBe(true); // At least one digit
    });

});
