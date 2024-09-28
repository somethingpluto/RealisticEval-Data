function containsPhoneNumber(s) {
    /**
     * Determines whether the string contains a phone number;
     * a possible format for a phone number is +1-800-555-1234, 555-555-1234, 555 555 1234
     */
    // Regex pattern to identify phone numbers
    const pattern = /(\+\d{1,3}[- ]?)?(\d{3}[- ]\d{3}[- ]\d{4})/;
    
    // Use pattern.test to find a match
    return pattern.test(s);
}

// Example usage:
console.log(containsPhoneNumber("+1-800-555-1234")); // true
console.log(containsPhoneNumber("This string has a phone number 555-555-1234 in it.")); // true
console.log(containsPhoneNumber("No phone number here!")); // false