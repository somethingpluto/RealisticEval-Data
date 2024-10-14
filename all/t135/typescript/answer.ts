/**
 * Checks if the provided port number is within the valid range of TCP/UDP ports.
 * Valid TCP/UDP port numbers range from 1 to 65535.
 *
 * @param {number} port - The port number to verify.
 * @returns {boolean} Returns true if the port number is valid, false otherwise.
 */
function isValidPortNumber(port: number): boolean {
    if (typeof port !== 'number' || isNaN(port) || Math.floor(port) !== port) {
        throw new TypeError('The port number must be an integer.');
    }

    return port >= 1 && port <= 65535;
}