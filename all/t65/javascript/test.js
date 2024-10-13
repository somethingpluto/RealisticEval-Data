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