function isCompliantIP(ip: string): boolean {
    /**
     * Check whether the IP address is a legal IP address.
     *
     * @param {string} ip - The IP address in string format.
     * @returns {boolean} - True if the IP is compliant, False otherwise.
     */

    // Regular expression to match a valid IPv4 address
    const ipRegex = /^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/;

    return ipRegex.test(ip);
}