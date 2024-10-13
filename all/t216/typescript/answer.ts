import * as child_process from 'child_process';
import * as re from 'xregexp';

function getLocalIP(interface: string = 'wlan0'): Promise<string> {
    return new Promise((resolve, reject) => {
        const command = ['ip', 'addr', 'show', interface].join(' ');
        
        child_process.exec(command, (error, stdout, stderr) => {
            if (error) {
                reject(new Error(`Failed to retrieve IP address: ${error.message}`));
                return;
            }

            // Regular expression to match IPv4 addresses, excluding the loopback address
            const ipPattern = re('inet (\\d+\\.\\d+\\.\\d+\\.\\d+)/\\d+', 'g');

            // Search for IP addresses in the command output
            const matches = stdout.match(ipPattern);

            if (matches && matches.length > 0) {
                resolve(matches[0].match(/(\d+\.\d+\.\d+\.\d+)/)![1]);
            } else {
                reject(new Error('No local IP found'));
            }
        });
    });
}