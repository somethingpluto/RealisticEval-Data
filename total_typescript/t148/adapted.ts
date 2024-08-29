function base64ToArrayBuffer(base64: string): ArrayBuffer {
    // Decode the base64 string into a binary string
    const binaryString = atob(base64);
    const length = binaryString.length;
    
    // Create a new ArrayBuffer with the same length as the binary string
    const buffer = new ArrayBuffer(length);
    
    // Create a view for the ArrayBuffer
    const bufferView = new Uint8Array(buffer);
    
    // Convert each character code from the binary string to Uint8Array
    for (let i = 0; i < length; i++) {
        bufferView[i] = binaryString.charCodeAt(i);
    }
    
    return buffer;
}
