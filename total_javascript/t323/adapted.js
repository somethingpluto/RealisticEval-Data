function isValidUsername(username) {
    // Define the regular expression for a valid username
    const usernameRegex = /^[a-zA-Z0-9_]+$/;

    // Test the username against the regular expression
    return usernameRegex.test(username);
}
