const { exec } = require('child_process');
const ipPattern = /\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b/g;

function getLocalIP(interface = 'Wi-Fi', callback) {
    /**
     * Retrieve the local IP address of the specified network interface on Windows.
     *
     * @param {string} interface - The name of the network interface to check (default is 'Wi-Fi').
     * @param {function} callback - A callback function to handle the result or error.
     */
    exec('ipconfig', (error, stdout, stderr) => {
        if (error) {
            console.error(`Error executing command: ${error}`);
            callback(null);
            return;
        }

        const matches = stdout.match(ipPattern);
        if (!matches) {
            console.error('No IP addresses found.');
            callback(null);
            return;
        }

        // Filter and return the first local IP starting with "192.168."
        const localIP = matches.find(ip => ip.startsWith('192.168.'));
        callback(localIP || null);
    });
}