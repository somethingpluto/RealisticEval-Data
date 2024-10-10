function findDuplicateIps(ipList: string[], ignoreList: string[]): string[] {
    /**
     * Find duplicate IPs in the given IP list excluding specified IPs to ignore.
     *
     * @param {string[]} ipList - List of IP addresses
     * @param {string[]} ignoreList - List of IP addresses to ignore
     *
     * @returns {string[]} A list of duplicate IPs excluding those in the ignore list.
     */

    const ipCounts = new Map<string, number>();
    for (const ip of ipList) {
        if (!ignoreList.includes(ip)) {
            ipCounts.set(ip, (ipCounts.get(ip) || 0) + 1);
        }
    }

    return Array.from(ipCounts.entries())
                .filter(([_, count]) => count > 1)
                .map(([ip]) => ip);
}