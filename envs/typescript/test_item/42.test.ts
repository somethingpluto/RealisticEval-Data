import { execSync } from 'child_process';

function replacePhoneNumbers(text: string): string {
  // Regex pattern to match US phone numbers in various formats
  const phoneRegex = /\b(?:\d{3}[-.]?\d{3}[-.]?\d{4}|\(\d{3}\)\s*\d{3}[-.]?\d{4}|\d{10})\b/g;

  // Replace all matches with '[PHONE_NUM]'
  return text.replace(phoneRegex, '[PHONE_NUM]');
}

// Function to call a Python script and pass the modified string
function callPythonScript(modifiedText: string): void {
  try {
    // Assuming the Python script is named 'process_text.py'
    execSync(`python process_text.py '${modifiedText}'`);
  } catch (error) {
    console.error('Error calling Python script:', error);
  }
}

// Example usage:
// const modifiedText = replacePhoneNumbers("Call me at 123-456-7890.");
// callPythonScript(modifiedText);
describe('TestReplacePhoneNumbers', () => {
    it('should replace a basic phone number', () => {
        const msg = "Call me at 123-456-7890.";
        const expected = "Call me at [PHONE_NUM].";
        expect(replacePhoneNumbers(msg)).toBe(expected);
    });

    it('should replace a phone number with parentheses', () => {
        const msg = "Our office number is 123 456-7890.";
        const expected = "Our office number is [PHONE_NUM].";
        expect(replacePhoneNumbers(msg)).toBe(expected);
    });

    it('should replace a phone number with dots', () => {
        const msg = "Fax us at 123.456.7890.";
        const expected = "Fax us at [PHONE_NUM].";
        expect(replacePhoneNumbers(msg)).toBe(expected);
    });

    it('should not replace anything when there is no phone number', () => {
        const msg = "Hello, please reply to this email.";
        const expected = "Hello, please reply to this email.";
        expect(replacePhoneNumbers(msg)).toBe(expected);
    });
});
