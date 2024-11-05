describe('TestFileSizeConverter', () => {

  test('test_bytes_less_than_1KB', () => {
    let result = convertFileSize(512)
    expect(["512B","512.00B"]).toContain(result)
  });

  test('test_exactly_1KB', () => {
    let result = convertFileSize(1024)
    expect(["1KB","1.00KB"]).toContain(result)
  });

  test('test_2KB', () => {
    let result = convertFileSize(2048)
    expect(["2KB","2.00KB"]).toContain(result)
  });

  test('test_exactly_1MB', () => {
    let result = convertFileSize(1048576)
    expect(["1MB","1.00MB"]).toContain(result)
  });

  test('test_5MB', () => {
    let result = convertFileSize(5242880)
    expect(["5MB","5.00MB"]).toContain(result)
  });

  test('test_exactly_1GB', () => {
    let result = convertFileSize(1073741824)
    expect(["1GB","1.00GB"]).toContain(result)
  });
});