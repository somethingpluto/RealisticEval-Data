function extractEmailDetails(email) {
    if (!email.includes('@')) {
        throw new Error("Invalid email address. Email must contain an '@' character.");
    }

    // Split the email at the '@' and assign parts to username and domain
    const [username, domain] = email.split('@');

    return [username, domain];
}