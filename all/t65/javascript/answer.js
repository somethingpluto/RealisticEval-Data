function findDuplicateIPs(ipList, ignoreList) {
  /**
   * Find duplicate IPs in the given IP list excluding specified IPs to ignore.
   *
   * @param {Array} ipList - List of IP addresses (strings).
   * @param {Array} ignoreList - List of IP addresses to ignore (strings).
   * @returns {Array} A list of duplicate IPs excluding those in the ignore list.
   */
  
  // Convert ignoreList to a Set for faster lookups
  const ignoreSet = new Set(ignoreList);

  // Object to count occurrences of each IP
  const ipCount = {};

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
  const duplicates = Object.entries(ipCount).filter(([ip, count]) => count > 1).map(([ip, count]) => ip);

  return duplicates;
}