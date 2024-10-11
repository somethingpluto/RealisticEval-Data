function extractSldTld(fqdn) {
    /**
     * Extracts the second-level and top-level domain names from the fully qualified domain name FQDN and returns them.
     * @param {string} fqdn - The fully qualified domain name.
     * @returns {Array<string>} - An array containing the second-level domain and top-level domain.
     */

    // Split the FQDN by dots
    const parts = fqdn.split('.');

    if (parts.length < 2) {
        throw new Error('Invalid FQDN');
    }

    // Get the top-level domain
    let tld = parts.pop();

    // If there is only one more part left, it's the second-level domain
    if (parts.length === 1) {
        return [parts[0], tld];
    } else {
        // Otherwise, join the remaining parts to form the second-level domain
        const sld = parts.join('.');
        return [sld, tld];
    }
}