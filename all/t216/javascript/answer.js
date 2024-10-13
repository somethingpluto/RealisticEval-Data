const { exec } = require('child_process');

function getLocalIP(interface = 'wlan0') {
    return new Promise((resolve, reject) => {
        // Execute the command to get the IP addresses from the specified interface
        const command = `ip addr show ${interface}`;
        exec(command, (error, stdout, stderr) => {
            if (error) {
                // Handle errors from the subprocess command
                reject(new Error(`Failed to retrieve IP address: ${error.message}`));
                return;
            }

            // Regular expression to match IPv4 addresses, excluding the loopback address
            const ipPattern = /inet (\d+\.\d+\.\d+\.\d+)\/\d+/;

            // Search for IP addresses in the command output
            const match = stdout.match(ipPattern);

            // Return the first valid IP found, or throw an error if no IP is found
            if (match) {
                resolve(match[1]);
            } else {
                reject(new Error("No local IP found"));
            }
        });
    });
}