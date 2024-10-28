describe('TestConvertHmsToMilliseconds', () => {
  test('test_basic_conversion', () => {
      expect(convertHmsToMilliseconds("1h20min30s")).toBe(4830000);
  });

  test('test_no_hours_or_minutes', () => {
      expect(convertHmsToMilliseconds("30s")).toBe(30000);
  });

  test('test_invalid_format', () => {
      expect(convertHmsToMilliseconds("1hour20minutes")).toBeNull();
  });

  test('test_edge_case_max_one_day', () => {
      expect(convertHmsToMilliseconds("23h59min59s")).toBe(86399000);
  });

  test('test_exceeding_one_day', () => {
      expect(convertHmsToMilliseconds("24h1min")).toBe(86460000);
  });
});