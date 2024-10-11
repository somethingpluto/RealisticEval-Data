/**
 * Invert the keys and values in an object. If multiple keys have the same value,
 * the new object's values will be an array of these keys.
 * @param originalObject - The object to invert.
 * @returns A new object with values and keys inverted.
 */
function invertDictionary<T extends Record<string, any>>(originalObject: T): { [K in keyof T]: K[] } {
    // Function implementation goes here
}