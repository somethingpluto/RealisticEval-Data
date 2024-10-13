function containsPhoneNumber(s: string): boolean {
    // Regex pattern to identify phone numbers
    const pattern = /(\+\d{1,3}[- ]?)?(\d{3}[- ]\d{3}[- ]\d{4})/;
    // Use RegExp test method to find a match
    return pattern.test(s);
}