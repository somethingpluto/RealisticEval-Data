function containsPhoneNumber(s) {
    /**
     * Determines whether the string contains a phone number; 
     * a possible format for a phone number is +1-800-555-1234, 555-555-1234, 555 555 1234
     */
    // Regex pattern to identify phone numbers
    const pattern = /(\+\d{1,3}[- ]?)?(\d{3}[- ]\d{3}[- ]\d{4})/;
    // Use RegExp test method to find a match
    return pattern.test(s);
}