function getLocalIP(interface = 'wlan0') {
    return new Promise((resolve, reject) => {
        exec(`ip addr show ${interface}`, (error, stdout, stderr) => {
            if (error) {
                console.error(`Error executing command: ${error.message}`);
                resolve('No IP found');
                return;
            }
            const regex = /inet\s+(\d+\.\d+\.\d+\.\d+)/g;
            let match;
            while ((match = regex.exec(stdout)) !== null) {
                resolve(match[1]);
                return;
            }
            resolve('No IP found');
        });
    });
}