function isValidEmail(email: string): boolean {
    // Define the regular expression for a valid email
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    // Test the email against the regular expression
    return emailRegex.test(email);
}