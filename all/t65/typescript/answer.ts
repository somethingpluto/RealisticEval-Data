function findDuplicateIPs(ipList: string[], ignoreList: string[]): string[] {
    // Convert ignoreList to a Set for faster lookups
    const ignoreSet = new Set(ignoreList);

    // Object to count occurrences of each IP
    const ipCount: Record<string, number> = {};

    // Count occurrences of each IP, excluding ignored IPs
    for (const ip of ipList) {
        if (!ignoreSet.has(ip)) {
            if (ip in ipCount) {
                ipCount[ip] += 1;
            } else {
                ipCount[ip] = 1;
            }
        }
    }

    // Collect duplicate IPs
    const duplicates = Object.entries(ipCount).filter(([ip, count]) => count > 1).map(([ip]) => ip);

    return duplicates;
}