// Importing the regex module is not required in TypeScript as it is built-in

function containsPhoneNumber(s: string): boolean {
    /**
     * Determines whether the string contains a phone number; a possible format for a phone number is +1-800-555-1234, 555-555-1234, 555 555 1234
     */
    // Regex pattern to identify phone numbers
    const pattern = /(\+\d{1,3}[- ]?)?(\d{3}[- ]\d{3}[- ]\d{4})/;
    // Use RegExp test method to find a match
    if (pattern.test(s)) {
        return true;
    } else {
        return false;
    }
}

// Example usage
const exampleString = "+1-800-555-1234";
console.log(containsPhoneNumber(exampleString)); // Should output: true