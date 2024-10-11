interface Dictionary {
  [key: string]: any;
}

function sanitizeData(data: Dictionary, keyToRemove?: string[]): Dictionary {
  // If no keys to remove were provided, return the original data
  if (!keyToRemove || keyToRemove.length === 0) {
    return data;
  }

  // Create a new object that will hold our sanitized data
  const sanitizedData: Dictionary = {};

  // Iterate over each key-value pair in the original data
  for (const [key, value] of Object.entries(data)) {
    // If the current key is not in the list of keys to remove, add it to the sanitized data
    if (!keyToRemove.includes(key)) {
      sanitizedData[key] = value;
    }
  }

  return sanitizedData;
}