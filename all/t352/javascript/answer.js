function hexStringToByteArray(hexStr) {
    // If the length of the hex string is odd, prepend a '0'
    if (hexStr.length % 2 === 1) {
        hexStr = "0" + hexStr;
    }

    // Convert hex string to bytes
    const length = hexStr.length;
    const data = new Uint8Array(length / 2);

    for (let i = 0; i < length; i += 2) {
        // Calculate the byte value from two hex characters
        data[i / 2] = (parseInt(hexStr[i], 16) << 4) + parseInt(hexStr[i + 1], 16);
    }

    return data; // Return Uint8Array
}