import * as child_process from 'child_process';
import * as re from 'xregexp';

/**
 * Gets the IPv4 address of the local computer on a specific network interface.
 * 
 * @param interface - The network interface to query. Default is 'wlan0'.
 * @returns A promise that resolves to the local IP address or rejects with an error message.
 */
function getLocalIP(interface: string = 'wlan0'): Promise<string> {}