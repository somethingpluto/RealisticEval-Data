describe('findDuplicateIPs', () => {
  it('should return duplicates excluding those in the ignore list', () => {
    const ipList = ['192.168.1.1', '10.0.0.1', '192.168.1.1', '172.16.0.1'];
    const ignoreList = ['10.0.0.1'];

    const result = findDuplicateIPs(ipList, ignoreList);

    expect(result).toEqual(['192.168.1.1']);
  });

  it('should handle empty input lists', () => {
    const ipList: string[] = [];
    const ignoreList: string[] = [];

    const result = findDuplicateIPs(ipList, ignoreList);

    expect(result).toEqual([]);
  });

  it('should handle no duplicates', () => {
    const ipList = ['192.168.1.1', '10.0.0.1', '172.16.0.1'];
    const ignoreList = ['10.0.0.1'];

    const result = findDuplicateIPs(ipList, ignoreList);

    expect(result).toEqual([]);
  });
});
