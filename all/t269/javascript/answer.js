function isCompliantIP(ip) {
    /**
     * Check whether the IP address is a legal IP address.
     *
     * @param {string} ip - The IP address in string format.
     * @returns {boolean} - True if the IP is compliant, False otherwise.
     */

    // Split the IP address into parts
    const parts = ip.split('.');

    // Check if there are exactly four parts
    if (parts.length !== 4) {
        return false;
    }

    // Validate each part of the IP address
    for (let i = 0; i < 4; i++) {
        const part = parseInt(parts[i], 10);

        // Check if the part is a number and within the valid range
        if (isNaN(part) || part < 0 || part > 255) {
            return false;
        }
    }

    // If all checks pass, the IP is compliant
    return true;
}