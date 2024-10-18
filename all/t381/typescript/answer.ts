function extractEmailDetails(email: string): [string, string] {
    /**
     * Extracts the username and mailbox suffix from an email address.
     *
     * @param email - the email address to extract details from
     * @returns A tuple [username, domain] where:
     *      username is the part before '@'
     *      domain is the part after '@'
     *
     * Example:
     *      extractEmailDetails("xxx@gmail.com") returns ['xxx', 'gmail.com']
     */

    // Check if '@' is in the email
    if (!email.includes('@')) {
        throw new Error("Invalid email address. Email must contain an '@' character.");
    }

    // Split the email at the '@' and assign parts to username and domain
    const [username, domain] = email.split('@', 1);

    return [username, domain];
}