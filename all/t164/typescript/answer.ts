/**
 * The Unit8 array is converted into 4 Base64 characters as a group of 3 bytes for processing, and the output of less than 3 is filled with =, and the resulting Base64 string is returned
 *
 * @param {Uint8Array} uint8Array - The Uint8Array to be converted.
 * @returns {string} - The resulting Base64-encoded string.
 */
function uint8ArrayToBase64(uint8Array: Uint8Array): string {
    let base64 = "";
    const characters =
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";

    for (let i = 0; i < uint8Array.length; i += 3) {
        const a = uint8Array[i];
        const b = uint8Array[i + 1] || 0;  // Use 0 if b is undefined
        const c = uint8Array[i + 2] || 0;  // Use 0 if c is undefined

        const index1 = a >> 2;
        const index2 = ((a & 0x03) << 4) | (b >> 4);
        const index3 = ((b & 0x0f) << 2) | (c >> 6);
        const index4 = c & 0x3f;

        base64 +=
            characters[index1] +
            characters[index2] +
            (i + 1 < uint8Array.length ? characters[index3] : "=") +
            (i + 2 < uint8Array.length ? characters[index4] : "=");
    }

    return base64;
}
