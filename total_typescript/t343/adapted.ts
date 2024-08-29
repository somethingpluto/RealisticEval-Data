function deepEqual(obj1: unknown, obj2: unknown): boolean {
  // Check for reference equality or if both are the same primitive
  if (obj1 === obj2) {
    return true;
  }

  // Check if only one is null or undefined
  if ((obj1 === null && obj2 !== null) || (obj1 !== null && obj2 === null)) {
    return false;
  }

  // Ensure both variables are of type 'object' (includes functions and arrays)
  if (typeof obj1 !== 'object' || typeof obj2 !== 'object' || obj1 === null || obj2 === null) {
    return false;
  }

  // Convert objects to key-value map arrays
  const entries1 = Object.entries(obj1 as Record<string, unknown>);
  const entries2 = Object.entries(obj2 as Record<string, unknown>);

  // If the number of keys is different, objects are not equal
  if (entries1.length !== entries2.length) {
    return false;
  }

  // Sort entries by key to ensure the order in comparison
  entries1.sort((a, b) => a[0].localeCompare(b[0]));
  entries2.sort((a, b) => a[0].localeCompare(b[0]));

  // Recursively compare each sorted key-value pair
  for (let i = 0; i < entries1.length; i++) {
    const [key1, value1] = entries1[i];
    const [key2, value2] = entries2[i];

    // Keys should be the same and the values must recursively be equal
    if (key1 !== key2 || !deepEqual(value1, value2)) {
      return false;
    }
  }

  // All checks passed, objects are deeply equal
  return true;
}