/**
 * Converts a standard Base64 encoded string into a URL-safe Base64 encoded string.
 *
 * @param {string} base64 - The standard Base64 encoded string to be converted.
 * @returns {string} The URL-safe Base64 encoded string.
 */
export function base64ToUrlSafe(base64) {
    // Replace "+" with "-", "/" with "_", and remove trailing "=" characters
    const urlSafeBase64 = base64
        .replace(/\+/g, "-")  // Replace all occurrences of "+" with "-"
        .replace(/\//g, "_")  // Replace all occurrences of "/" with "_"
        .replace(/=+$/, "");  // Remove any trailing "=" characters

    return urlSafeBase64;
}