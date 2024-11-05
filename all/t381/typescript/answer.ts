function extractEmailDetails(email: string): [string, string] {
    if (!email.includes('@')) {
        throw new Error("Invalid email address. Email must contain an '@' character.");
    }

    // Split the email at the '@' and assign parts to username and domain
    const [username, domain] = email.split('@');

    // Return a tuple of username and domain
    if (!domain) {
        throw new Error("Invalid email address. Domain part is missing.");
    }

    return [username, domain];
}
