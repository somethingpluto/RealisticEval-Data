/**
 * Retrieve the local IP address of the specified network interface on Windows.
 *
 * @param {string} interfaceName - The name of the network interface to check (default is 'Wi-Fi').
 * @returns {Promise<string | null>} A promise that resolves to the local IP address if found, otherwise null.
 */
function getLocalIp(interfaceName: string = 'Wi-Fi'): Promise<string | null> {

}