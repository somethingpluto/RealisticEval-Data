import * as childProcess from 'child_process';
import * as re from 'xregexp';

function getLocalIp(interfaceName: string = 'Wi-Fi'): Promise<string | null> {
    return new Promise((resolve, reject) => {
        // Execute the 'ipconfig' command to get addresses for the specified interface
        childProcess.exec('ipconfig', (error, stdout, stderr) => {
            if (error) {
                console.error(`Error executing command: ${error}`);
                resolve(null);
                return;
            }

            // Regular expression to match IPv4 addresses
            const ipPattern = re('(?:\\d{1,3}\\.){3}\\d{1,3}', 'g');

            // Search for IP addresses in the command output
            const ips: string[] = re.match(stdout, ipPattern, 'all');

            // Return the first local IP found
            for (const ip of ips) {
                if (ip.startsWith('192.168.')) {
                    resolve(ip);
                    return;
                }
            }

            resolve(null); // Return null if no suitable IP is found
        });
    });
}