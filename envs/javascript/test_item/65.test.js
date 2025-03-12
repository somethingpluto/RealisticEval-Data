/**
 * Find duplicate IPs in the given IP list excluding specified IPs to ignore.
 *
 * @param {string[]} ipList - List of IP addresses.
 * @param {string[]} ignoreList - List of IP addresses to ignore.
 * @returns {string[]} A list of duplicate IPs excluding those in the ignore list.
 */
function findDuplicateIPs(ipList, ignoreList) {
    const ipCountMap = new Map();
    const duplicates = new Set();

    // Count occurrences of each IP
    for (const ip of ipList) {
        if (ipCountMap.has(ip)) {
            ipCountMap.set(ip, ipCountMap.get(ip) + 1);
        } else {
            ipCountMap.set(ip, 1);
        }
    }

    // Identify duplicates excluding those in the ignore list
    for (const [ip, count] of ipCountMap.entries()) {
        if (count > 1 && !ignoreList.includes(ip)) {
            duplicates.add(ip);
        }
    }

    // Convert Set to Array
    return Array.from(duplicates);
}
describe('TestFindDuplicateIPs', () => {
  it('should handle basic duplicates', () => {
      const ipList = ["192.168.1.1", "192.168.1.2", "192.168.1.1"];
      const ignoreList = [];
      expect(findDuplicateIPs(ipList, ignoreList)).toEqual(["192.168.1.1"]);
  });

  it('should handle ignored duplicates', () => {
      const ipList = ["192.168.1.1", "192.168.1.1", "192.168.1.2"];
      const ignoreList = ["192.168.1.1"];
      expect(findDuplicateIPs(ipList, ignoreList)).toEqual([]);
  });

  it('should handle no duplicates', () => {
      const ipList = ["192.168.1.1", "192.168.1.2", "192.168.1.3"];
      const ignoreList = [];
      expect(findDuplicateIPs(ipList, ignoreList)).toEqual([]);
  });

  it('should handle mixed duplicates', () => {
      const ipList = ["192.168.1.1", "192.168.1.1", "10.0.0.1", "192.168.1.2"];
      const ignoreList = ["192.168.1.2"];
      expect(findDuplicateIPs(ipList, ignoreList)).toEqual(["192.168.1.1"]);
  });

  it('should handle empty input', () => {
      const ipList = [];
      const ignoreList = [];
      expect(findDuplicateIPs(ipList, ignoreList)).toEqual([]);
  });

  it('should handle only ignored IPs', () => {
      const ipList = ["192.168.1.1", "192.168.1.1"];
      const ignoreList = ["192.168.1.1"];
      expect(findDuplicateIPs(ipList, ignoreList)).toEqual([]);
  });

  it('should handle all duplicates', () => {
      const ipList = ["192.168.1.1", "192.168.1.1", "192.168.1.1"];
      const ignoreList = [];
      expect(findDuplicateIPs(ipList, ignoreList)).toEqual(["192.168.1.1"]);
  });
});
