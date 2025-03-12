// Start of the TypeScript code
import { exec } from 'child_process';

function containsPhoneNumber(s: string): boolean {
  // ... (rest of the TypeScript function remains unchanged)

  // After the TypeScript function
  if (matches.length > 0) {
    exec(`python3 log_phone_number.py "${matches[0]}"`, (error, stdout, stderr) => {
      if (error) {
        console.error(`exec error: ${error}`);
        return;
      }
      console.log(`Python script output: ${stdout}`);
    });
  }
}
// End of the TypeScript code
describe('containsPhoneNumber', () => {
    it('should detect international prefix', () => {
        expect(containsPhoneNumber('+1-800-555-1234')).toBe(true);
    });

    it('should detect standard format with dashes', () => {
        expect(containsPhoneNumber('800-555-1234')).toBe(true);
    });

    it('should detect standard format with spaces', () => {
        expect(containsPhoneNumber('800 555 1234')).toBe(true);
    });

    it('should not detect any phone number', () => {
        expect(containsPhoneNumber('Hello, world!')).toBe(false);
    });

    it('should detect phone number in text', () => {
        expect(containsPhoneNumber('Call me at 800-555-1234 today!')).toBe(true);
    });
});
