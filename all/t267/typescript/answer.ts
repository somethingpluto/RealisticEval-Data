function extractSldTld(fqdn: string): [string, string] {
    /**
     * Extracts the second-level and top-level domain names from the fully qualified domain name FQDN and returns them.
     * @param fqdn - The fully qualified domain name.
     * @returns A tuple containing the second-level domain and top-level domain.
     */

    const parts = fqdn.split('.');

    if (parts.length < 2) {
        throw new Error('Invalid FQDN');
    }

    const tld = parts[parts.length - 1];
    let sld = '';

    if (parts.length === 3) {
        sld = `${parts[0]}.${parts[1]}`;
    } else {
        sld = parts.slice(0, parts.length - 2).join('.');
    }

    return [sld, tld];
}