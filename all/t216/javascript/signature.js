const { exec } = require('child_process');

/**
 * Gets the IPv4 address of the local computer on a specific network interface, such as wlan0, which is usually a wireless network interface.
 * @param {string} [interface='wlan0'] - The network interface to query. Default is 'wlan0'.
 * @returns {Promise<string>} A promise that resolves to the local IP address, or a message indicating no IP was found.
 */
function getLocalIP(interface = 'wlan0') {}