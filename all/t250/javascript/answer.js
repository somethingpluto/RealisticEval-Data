function invertDictionary(originalDict) {
  /**
   * Invert the keys and values in an object. If multiple keys have the same value,
   * the new object's values will be an array of these keys.
   *
   * @param {Object} originalDict - The object to invert.
   * @returns {Object} A new object with values and keys inverted.
   */
  const newDict = {};
  for (const [key, value] of Object.entries(originalDict)) {
      if (!newDict.hasOwnProperty(value)) {
          newDict[value] = key;
      } else {
          // If the value already exists as a key, we need to append to or create an array
          if (!Array.isArray(newDict[value])) {
              newDict[value] = [newDict[value]];
          }
          newDict[value].push(key);
      }
  }
  return newDict;
}