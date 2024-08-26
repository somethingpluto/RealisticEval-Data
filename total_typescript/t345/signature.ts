/**
 * Convert an object to a URL query string and recursively process every attribute of the object, including basic data types, arrays, and nested objects. For arrays and nested objects, build key-value pairs strings in a format suitable for URL query parameters, such as key[index][subKey]=value
 * @param obj
 */
function toQueryString(obj: Record<string, unknown>): string {

}