describe('findDuplicateIps', () => {
  it('should return an empty array when no duplicates and no ignored IPs', () => {
    const ipList = ['192.168.1.1', '10.0.0.1'];
    const ignoreList = [];
    expect(findDuplicateIps(ipList, ignoreList)).toEqual([]);
  });

  it('should return an empty array when all IPs are ignored', () => {
    const ipList = ['192.168.1.1', '10.0.0.1'];
    const ignoreList = ['192.168.1.1', '10.0.0.1'];
    expect(findDuplicateIps(ipList, ignoreList)).toEqual([]);
  });

  it('should return a list of duplicates excluding ignored IPs', () => {
    const ipList = ['192.168.1.1', '192.168.1.1', '10.0.0.1', '10.0.0.1', '172.16.0.1'];
    const ignoreList = ['192.168.1.1', '10.0.0.1'];
    expect(findDuplicateIps(ipList, ignoreList)).toEqual(['172.16.0.1']);
  });
});