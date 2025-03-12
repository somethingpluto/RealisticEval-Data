import { IPMap } from './IPMap'; // Assuming IPMap is a class that maps IPs to their count

function findDuplicateIPs(ipList: string[], ignoreList: string[]): string[] {
  const ipMap = new IPMap();
  const duplicates: string[] = [];
  const ignoredIPs = new Set(ignoreList);

  ipList.forEach(ip => {
    if (!ignoredIPs.has(ip)) {
      ipMap.update(ip);
    }
  });

  ipMap.forEach((count, ip) => {
    if (count > 1) {
      duplicates.push(ip);
    }
  });

  return duplicates;
}
describe('findDuplicateIPs', () => {
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
