function toQueryString(obj: Record<string, unknown>): string {
  // Helper function to handle different data types
  function handleValue(key: string, value: unknown, prefix: string = ''): string {
    const fullKey = prefix ? `${prefix}[${encodeURIComponent(key)}]` : encodeURIComponent(key);

    if (Array.isArray(value)) {
      return value.map((v, i) => handleValue(String(i), v, fullKey)).join('&');
    } else if (typeof value === 'object' && value !== null) {
      return Object.entries(value as Record<string, unknown>)
        .map(([subKey, subVal]) => handleValue(subKey, subVal, fullKey))
        .join('&');
    } else {
      return `${fullKey}=${encodeURIComponent(String(value))}`;
    }
  }

  // Combine all entries into a query string
  return Object.entries(obj)
    .map(([key, value]) => handleValue(key, value))
    .join('&');
}