async function getLocalIp(interface: string = 'wlan0'): Promise<string> {
    /**
     * Gets the IPv4 address of the local computer on a specific network interface, such as wlan0,
     * which is usually a wireless network interface.
     *
     * @param {string} [interface='wlan0'] - The network interface to query. Default is 'wlan0'.
     * @returns {Promise<string>} - A promise that resolves with the local IP address, or a message indicating no IP was found.
     */
    
    try {
        const { stdout } = await execAsync(`ifconfig ${interface}`);
        const ipMatch = stdout.match(/inet\s+(\d+\.\d+\.\d+\.\d+)/);
        
        if (ipMatch && ipMatch[1]) {
            return ipMatch[1];
        } else {
            throw new Error('No IP address found');
        }
    } catch (error) {
        console.error(error.message);
        return 'No IP address found';
    }
}